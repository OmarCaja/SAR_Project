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

def load_index(index_dir):
    return 0

def parse_query(query):
    especial_char = re.compile(r'[\(\)]')
    query = especial_char.sub(r' \g<0> ', query)
    query_list = query.split()
    
    return query_list

def search(parsed_query):
    return 0

def search_and_print(text):
        parsed_query = parse_query(query)
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

