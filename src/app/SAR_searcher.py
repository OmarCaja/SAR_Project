'''
Proyecto de Practicas SAR: searcher

Autores:

Omar Caja Garcia
Zhihao Zhang
Pablo Lopez Orrios
Jose Antonio Culla de Moya

Ampliaciones:
query con parentesis
multiples indices
ordenacion de los resultados
busqueda de terminos consecutivos
'''
import argparse
import json
import math
import re

from data_structures.data_structures_handler import import_news_index
from read_data.reader import get_json_data, clean_text
from words_distance.branch_and_bound.word_to_trie import damerau_levenshtein
from words_distance.branch_and_bound.word_to_trie import levenshtein

indexes = {}
tries = {}
article_searched = False
query_terms = []


def load_json(filename):
    with open(filename) as fh:
        obj = json.load(fh)
    return obj


def opAND(list1, list2):
    i = 0
    j = 0
    res = list()
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            res.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            i += 1
        else:
            j += 1
    return res


def opOR(list1, list2):
    i = 0
    j = 0
    res = list()
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            res.append(list1[i])
            i += 1
            j += 1
        elif list1[i] < list2[j]:
            res.append(list1[i])
            i += 1
        else:
            res.append(list2[j])
            j += 1
    if i == len(list1):
        aux = j
        aux2 = list2
    else:
        aux = i
        aux2 = list1
    while aux < len(aux2):
        res.append(aux2[aux])
        aux += 1
    return res


# param: num = numero de docid
def opNOT(lista):
    i = 0
    j = 0
    doc = list(indexes.get("docs", {}).keys())
    res = []
    while i < len(lista):
        if doc[j] == lista[i]:
            j += 1
            i += 1
        elif doc[j] < lista[i]:
            res.append(doc[j])
            j += 1
        else:
            i += 1
    while j < len(doc):
        res.append(doc[j])
        j += 1
    return res


def preproces_query(query):
    for quoted_part in re.findall(r'\"(.+?)\"', query):
        query = query.replace(quoted_part, quoted_part.replace(" ", "\""))
    return query


# query:una lista donde contiene los terminos
# lista: lista resultado donde contiene docid
# peso que usamos es lnc.ltc(lo mismo que la trasparencia de teoria)
# devuelve una lista de lista,tiene siguiente formato
# [[docid,peso],[docid,peso]...]ordenado de mayor a menor
def ranking(query, lista):
    global indexes
    article_index = indexes.get("article", {})
    doc_news_index = indexes.get("docs", {})
    queryWeight = dict()
    docWeight = dict()
    res = dict()
    # obtener frecuencia de cada termino del query
    for term in query:
        queryWeight[term] = queryWeight.get(term, 0.0) + 1.0
    # inicializar docWeight
    for doc in lista:
        docWeight[doc] = dict()
    # calcular w de cada termino para cada doc y query
    for term in queryWeight.keys():
        f = queryWeight[term]
        tf = 1.0 + math.log(f, 10)
        df = len(article_index.get(term, list()))
        if (df != 0):
            idf = math.log(float(len(doc_news_index)) / df, 10.0)
        else:
            idf = 0
        queryWeight[term] = idf * tf
        for doc in lista:
            f = article_index.get(term, {}).get(doc, 0)
            if f != 0:
                f = f[0]
            if (f == 0):
                docWeight[doc][term] = 0
                continue
            tf = 1.0 + math.log(f, 10)
            docWeight[doc][term] = tf

    # normalizar query
    wTotal = 0
    for w in queryWeight.values():
        wTotal += math.pow(w, 2.0)
    wTotal = math.sqrt(wTotal)
    for term in queryWeight.keys():
        if (wTotal != 0):
            queryWeight[term] /= wTotal
    # calcula la puntuacion
    for doc in docWeight:
        for term in queryWeight.keys():
            res[doc] = res.get(doc, 0) + queryWeight[term] * docWeight[doc][term]

    return sort_by_value(res)


def sort_by_value(d):
    items = d.items()
    backitems = [[v[1], v[0]] for v in items]
    backitems.sort(reverse=True)
    return [[backitems[i][1], backitems[i][0]] for i in range(0, len(backitems))]


operators = {
    'AND': 2,
    'OR': 2,
    'NOT': 3,
    '(': 1,
    ')': 4
}


def load_index(index_file):
    indeces = import_news_index(index_file)
    (article_index, title_index, keyword_index, date_index, summary_index, doc_news_index) = indeces
    global indexes
    indexes = {
        "article": article_index,
        "title": title_index,
        "keywords": keyword_index,
        "date": date_index,
        "summary": summary_index,
        "docs": doc_news_index
    }


def load_trie(trie_file):
    trie = import_news_index(trie_file)
    (article_trie, title_trie, keyword_trie, date_trie, summary_trie) = trie
    global tries
    tries = {
        "article": article_trie,
        "title": title_trie,
        "keywords": keyword_trie,
        "date": date_trie,
        "summary": summary_trie,
    }


def parse_query(query):
    output = []
    stack = []
    especial_char = re.compile(r'[\(\)]')
    query = especial_char.sub(r' \g<0> ', query)
    token_list = query.split()

    for token in token_list:
        if operators.get(token, False) and token != ')':
            while len(stack) != 0 and token != '(' and operators[stack[0]] >= operators[token]:
                output.append(stack.pop(0))
            stack.insert(0, token)
        elif token == ')':
            operator = stack.pop(0)
            while operator != '(':
                if (len(stack) == 0):
                    print("error: mismatch parentheses")
                    break
                output.append(operator)
                operator = stack.pop(0)
        else:
            output.append(token)

    while (len(stack) != 0):
        operator = stack.pop(0)
        if (operator == ')'):
            print("error: mismatch parentheses")
            break
        output.append(operator)

    return output


def search(query):
    stack = []
    query_words = []
    for item in query:
        if item == 'NOT':
            opres = opNOT(stack.pop(0))
            stack.insert(0, opres)
        elif item == 'AND':
            opres = opAND(stack.pop(0), stack.pop(0))
            stack.insert(0, opres)
        elif item == 'OR':
            opres = opOR(stack.pop(0), stack.pop(0))
            stack.insert(0, opres)
        else:
            (terms, posting) = get_posting_list(item)
            query_words.append(terms)
            stack.insert(0, list(posting))

    global query_terms
    query_terms = [term for sublist in query_words for term in sublist]
    return ranking(query_terms, stack.pop(0))


def get_posting_list(item):
    global article_searched
    terms = []
    sol_dict = set()

    if (item.rfind(":") != -1):
        dict = item.split(":")[0]
        term = item.split(":")[1]

        words = []
        item_with_tolerance = term.lower()
        extract_tolerance_damerau = item_with_tolerance.split('@')
        extract_tolerance_levenshtein = item_with_tolerance.split('%')

        if (len(extract_tolerance_damerau) > 1):
            words = damerau_levenshtein(extract_tolerance_damerau[0], tries.get(dict, {}), extract_tolerance_damerau[1])

        elif (len(extract_tolerance_levenshtein) > 1):
            words = levenshtein(extract_tolerance_levenshtein[0], tries.get(dict, {}), extract_tolerance_levenshtein[1])

        else:
            words.append(term.lower())

        if (re.match(r'^"', term)):
            term_list = re.sub(r'"', " ", term).split()
            terms = term_list
            sol_dict = positional_search(term_list, dict)
        else:
            for word in words:
                article_searched = word == "article"
                for key in indexes.get("article", {}).get(word, {}).keys():
                    sol_dict.add(key)
                terms.append(word)

    elif (re.match(r'^"', item)):
        article_searched = True
        term_list = re.sub(r'"', " ", item).split()
        terms = term_list
        sol_dict = positional_search(term_list, "article")
    else:
        words = []
        item_with_tolerance = item.lower()
        extract_tolerance_damerau = item_with_tolerance.split('@')
        extract_tolerance_levenshtein = item_with_tolerance.split('%')

        if (len(extract_tolerance_damerau) > 1):
            words = damerau_levenshtein(extract_tolerance_damerau[0], tries.get("article", {}),
                                        extract_tolerance_damerau[1])

        elif (len(extract_tolerance_levenshtein) > 1):
            words = levenshtein(extract_tolerance_levenshtein[0], tries.get("article", {}),
                                extract_tolerance_levenshtein[1])

        else:
            words.append(item.lower())

        for word in words:
            article_searched = True
            for key in indexes.get("article", {}).get(word, {}).keys():
                sol_dict.add(key)
            terms.append(word)

    res = sorted(list(sol_dict))
    return (terms, res)


def positional_search(term_list, dict):
    index = indexes.get(dict, {})
    posting_lists = []
    for term in term_list:
        posting = index.get(term, {})
        lista = []
        for key in posting.keys():
            aux = []
            aux.append(key)
            aux.append(posting[key][1])
            lista.append(aux)
        posting_lists.append(lista)

    posting_lists.insert(0, positional_intersecction(posting_lists.pop(0), posting_lists.pop(0)))

    while (len(posting_lists) > 1):
        posting_lists.append(positional_intersecction(posting_lists.pop(0), posting_lists.pop(0)))

    return [list[0] for list in posting_lists.pop(0)]


def positional_intersecction(list1, list2):
    result = {}
    k = 1
    i = 0
    j = 0
    while (i < len(list1) and j < len(list2)):
        if (list1[i][0] == list2[j][0]):
            aux_list = []
        pp1 = list1[i][1]
        pp2 = list2[j][1]
        for pos_pp1 in pp1:
            for pos_pp2 in pp2:
                if (abs(pos_pp1 - pos_pp2) <= k):
                    aux_list.append(pos_pp2)
                elif pos_pp2 > pos_pp1:
                    break
            while ((len(aux_list) != 0) and (abs(aux_list[0] - pos_pp1) > k)):
                aux_list.pop(0)
            for ps in aux_list:
                result.setdefault(list1[i][0], []).append(ps)
        i += 1
        j += 1
    else:

        if list1[i][0] < list2[j][0]:
            i += 1
        else:
            j += 1

    res = [[k, v] for k, v in result.items()]

    return res


def search_and_print(text):
    query = preproces_query(text)
    parsed_query = parse_query(query)
    doc_list = search(parsed_query)
    res = get_doc_info(doc_list)
    show_result(res)


# pasar una lista de [doc_id,puntuacion](obtenida de la funcion ranking()),y un num indica cuando doc quieres recuperar
# devuelve una lista de [art,puntuacion]
def get_doc_info(lista):
    res = []
    for doc in lista:
        obj = indexes.get("docs", {})[doc[0]]
        documento = get_json_data(obj[0])
        for art in documento:
            if (art["id"] == obj[1]):
                res.append([art, doc[1]])
                break
    return res


# pasa la lista obtenida de la funcion get_doc_info [art,puntuacion]
def show_result(lista):
    n = len(lista)
    if (n <= 2):
        for art in lista:
            print("puntuacion: ", art[1])
            print("fecha: ", art[0]["date"])
            print("titulo: ", art[0]["title"])
            print("keywords: ", art[0]["keywords"])
            print("articulo: ", art[0]["article"], "\n")
    elif (n <= 5):
        for art in lista:
            print("puntuacion: ", art[1])
            print("fecha: ", art[0]["date"])
            print("titulo: ", art[0]["title"])
            print("keywords: ", art[0]["keywords"])
            contenido = get_snippet(art[0]["article"])

            if (not article_searched):
                i = 0
                for c in art[0]["article"].split():
                    if (i >= 100):
                        break
                    contenido += c
                    contenido += " "
                    i += 1

            print("Snippets: ", contenido, "\n")
    else:
        i = 0
        for art in lista:
            if (i >= 10):
                break
            print("puntuacion", art[1], "   fecha: ", art[0]["date"], "   titulo: ", art[0]["title"], "   keywords: ",
                  art[0]["keywords"], "\n")
            i += 1
    print("Noticias recuperadas: ", n)


def get_snippet(article):
    res = ""
    frase = ""
    queryDict = dict()
    art = clean_text(article)
    for term in query_terms:
        queryDict[term.lower()] = True
    i = 0
    art = art.lower()
    art = art.split()
    for term in art:
        if (queryDict.get(term, False)):
            queryDict[term] = False
            frase = ""
            for j in range(20):
                k = i + (j - 10)
                if (k >= 0 and k < len(art)):
                    frase += art[k]
                    frase += " "
            frase += "\n"
            res += frase
        i += 1
    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("index", help="index file")
    parser.add_argument("-q", help="query to search")

    args = parser.parse_args()

    load_index(args.index)
    load_trie(args.index + "_trie")

    if args.q:
        search_and_print(args.q)
    else:
        while True:
            query = input("Introduzca una consulta: ")
            if len(query) == 0:
                break
            search_and_print(query)
