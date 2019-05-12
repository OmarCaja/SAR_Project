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


def opAND(list1,list2):
    i = 0
    j = 0
    res = list()
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
def opAND(list1,list2,caso):
    if caso == 1:
        si = list2
        no = list1
    else:
        si = list1
        no = list2

    res = list()
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
        res.append[si[i]]
        i+=1
    return res


def opOR(list1,list2):
    i = 0
    j = 0
    res = list()
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
def opNOT(num,list):
    i = 0
    j = 0
    res = list()
    while i < len(list):
        if j == list[i]:
            j+=1
            i+=1
        elif j < i:
            res.append(j)
            j+=1
        else:
            i+=1
    while j < num:
        res.append(j)
        j+=1
    return res
         

operators = {
    'AND': 2, 
    'OR': 2, 
    'NOT': 3, 
    '(': 1, 
    ')': 4 
    }

def load_index(index_dir):
    return 0

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
    result = []
    for item in query:
        if operators.get(item, False):
            stack.insert(0, item)
        elif item == 'NOT':
            opNOT(20, stack.pop(0))
        elif item == 'AND':
            pass
        elif item == 'OR':
            pass
    return 0

def search_and_print(text):
        parsed_query = parse_query(query)
        print(parsed_query)
        search(parsed_query)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("index", help="index directory")
    parser.add_argument("-q", help="query to search")

    args = parser.parse_args()

    index = load_index(args.index)

    if args.q:
        search_and_print(args.q)
    else:
        while True:
            query = raw_input("Introduzca una consulta: ")
            if len(query) == 0:
                break
            search_and_print(query)

