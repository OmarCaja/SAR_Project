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
import pickle
import re
import json

doc_id = -1
new_pos_in_doc = -1

directory_path = '/'

clean_re = re.compile('\\W+')


def clean_text(text):

    return clean_re.sub(' ', text)


def get_doc_id():

    global doc_id
    doc_id += 1
    return doc_id


def get_new_pos_in_doc():

    global new_pos_in_doc
    new_pos_in_doc += 1
    return new_pos_in_doc


def get_json_data(filename):

    with open(filename, "r") as json_file:
        return json.load(json_file)


def index_value_from_json(json_data, key):

    for new in json_data:
        print(new[key])
        print(get_new_pos_in_doc())


def index_files_from_directory(directory):

    for filename in os.listdir(directory):

        print(get_doc_id())
        print(filename)

        json_data = get_json_data(directory + directory_path + filename)
        index_value_from_json(json_data, 'article')

        global new_pos_in_doc
        new_pos_in_doc = -1


def save_index(index, filename):

    with open(filename, "wb") as fh:
        pickle.dump(index, fh)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="News directory")
    parser.add_argument("index", help="Index name")

    args = parser.parse_args()

    docs_directory = args.directory
    index_name = args.index
    index = {}

    index_files_from_directory(docs_directory)

    save_index(index, index_name)
