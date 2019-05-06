#!/usr/bin/python3

'''
Proyecto de Prácticas SAR: indexer
Autores:
Omar Caja García
Zhihao Zhang
Pablo López Orrios
Jose Antonio Culla de Moya
'''

import sys
import os
import argparse

doc_id = -1

def get_doc_id():

    global doc_id
    doc_id += 1
    return doc_id

def get_files_from_directory(directory):

    for filename in os.listdir(directory):

        print(get_doc_id())
        print(filename)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help = "News directory")
    parser.add_argument("index", help = "Index name")

    args = parser.parse_args()

    directory = args.directory
    index = args.index

    get_files_from_directory(directory)

    