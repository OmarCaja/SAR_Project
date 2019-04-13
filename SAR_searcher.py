'''
Proyecto de Prácticas SAR: indexer
Autores:
Omar Caja García
Zhihao Zhang
Pablo López Orrios
Jose Antonio Culla de Moya 
'''

import argparse

def load_index(index_dir):
    return 0

def parse_query(query):
    return 0

def search(parses_query):
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

