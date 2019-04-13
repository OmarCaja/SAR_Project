'''
Proyecto de Practicas SAR: indexer
Autores:
Omar Caja Garcia
Zhihao Zhang
Pablo Lopez Orrios
Jose Antonio Culla de Moya 
'''

import argparse
import re

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

def search(parsed_query):
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

