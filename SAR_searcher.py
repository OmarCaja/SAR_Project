#!/usr/bin/python3

'''
Proyecto de Practicas SAR: indexer
Autores:
Omar Caja Garcia
Zhihao Zhang
Pablo Lopez Orrios
Jose Antonio Culla de Moya 
'''
import sys
import argparse
import re
import json
import os
import pickle

term_index = {}
doc_index = {}

def load_json(filename):
    with open(filename) as fh:
        obj = json.load(fh)
    return obj

def get_json_data(doc_name):

    with open(doc_name, "r") as json_file:

        return json.load(json_file)

def opAND(l1,l2):
    i = 0
    j = 0
    res = list()
    list1 = l1.keys()
    list2 = l2.keys()
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            res.append(list1[i])
            i+=1
            j+=1
        elif list1[i]< list2[j]:
            i+=1
        else:
            j+=1
    return res

#por eficiencia,cuando (l1 and notl2) o (notl1 and l2) se calcula con esta funcion
#caso = 1 (notl1 and l2)
#caso = 2 (l1 and notl2)
def opANDNOT(list1,list2,caso):
    if caso == 1:
        si = list2
        no = list1
    else:
        si = list1
        no = list2

    res = []
    i = 0
    j = 0
    while i < len(si) and j < len(no):
        if si[i] == no[j]:
            i+=1
            j+=1
        elif si[i] <no[j]:
            res.append(si[i])
            i+=1
        else:
            j+=1
    while i < len(si):
        res.append(si[i])
        i+=1
    return res


def opOR(l1,l2):
    i = 0
    j = 0
    res = list()
    list1 = l1.keys()
    list2 = l2.keys()
    while i < len(list1) and j < len(list2):
        if list1[i] == list2[j]:
            res.append(list1[i])
            i+=1
            j+=1
        elif list1[i]< list2[j]:
            res.append(list1[i])
            i+=1
        else:
            res.append(list2[j])
            j+=1
    if i == len(list1):
        aux = j
        aux2 = list2
    else:
        aux = i
        aux2 = list1
    while aux < len(aux2):
        res.append(aux2[aux])
        aux+=1
    return res


#param: num = numero de docid
def opNOT(l):
    i = 0
    j = 0
    doc = doc_index.keys()
    res = []
    lista = l.keys()
    while i < len(lista):
        if doc[j] == lista[i]:
            j+=1
            i+=1
        elif j < i:
            res.append(doc[j])
            j+=1
        else:
            i+=1
    while j < len(doc):
        res.append(doc[j])
        j+=1
    return res
         

operators = {
    'AND': 2, 
    'OR': 2, 
    'NOT': 3, 
    '(': 1, 
    ')': 4 
    }

def load_index(index_file):
    with open(index_file, "rb") as fh:
        indeces = pickle.load(fh)
        global term_index
        global doc_index
        (term_index, doc_index) = indeces
            


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
            stack.insert(0, term_index.get(item,[]))
    return stack.pop(0)

def search_and_print(text):
        parsed_query = parse_query(query)
        doc_list = search(parsed_query)
        res = get_doc_info(doc_list)
        show_result(res)

#pasar una lista con doc_id,y un num indica cuando doc quieres recuperar
#devuelve una lista que estan dato json del num primer doc_id
def get_doc_info(lista):
    res = []
    for doc in lista:
        obj  = doc_index[doc]
        documento = get_json_data(obj[0])
        for art in documento:
            if(art["id"] == obj[1]):
                res.append(art)
                break
    return res

#pasa la lista obtenida de la funcion get_doc_info
def show_result(lista):
    n = len(lista)
    if(n <= 2):
        for art in lista:
            print("fecha: ",art["date"])
            print("titulo: ",art["title"])
            print("keywords: ",art["keywords"])
            print("articulo: ",art["article"])
    elif(n<=5):
        for art in lista:
            print("fecha: ",art["date"])
            print("titulo: ",art["title"])
            print("keywords: ",art["keywords"])
            contenido = ""
            i = 0
            for c in art["article"]:
                if(i >= 100):
                    break
                contenido+=c
            print(c)
    else:
        i = 0
        for art in lista:
            if(i >= 10):
                break
            print("fecha: ",art["date"],"   titulo: ",art["title"],"   keywords: ",art["keywords"])
    print(n)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("index", help="index file")
    parser.add_argument("-q", help="query to search")

    args = parser.parse_args()

    load_index(args.index)

    if args.q:
        search_and_print(args.q)
    else:
        while True:
            query = raw_input("Introduzca una consulta: ")
            if len(query) == 0:
                break
            search_and_print(query)

