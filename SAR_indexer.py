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

term_index = {}
doc_new_index = {}

doc_new_index_save_name = 'doc_new_index'

doc_id = 0
new_pos_in_doc = 0
doc_id_news_id_separator = '_'

directory_path = '/'

json_new_article = 'article'
json_new_id = 'id'

clean_re = re.compile('\\W+')


def clean_text(text):

    return clean_re.sub(' ', text)


def get_doc_id():

    return doc_id


def increase_doc_id():

    global doc_id
    doc_id += 1


def get_new_pos_in_doc():

    return new_pos_in_doc


def increase_new_pos_id():

    global new_pos_in_doc
    new_pos_in_doc += 1


def reset_new_pos_in_doc():

    global new_pos_in_doc
    new_pos_in_doc = -1


def get_new_key():

    return str(get_doc_id()) + doc_id_news_id_separator + str(get_new_pos_in_doc())


def get_json_data(doc_name):

    with open(doc_name, "r") as json_file:

        return json.load(json_file)


def index_word(word):

    list_values = term_index.get(word)

    if list_values == None:

        list_values = []
        list_values.append(get_new_key())

        term_index[word] = list_values

    else:

        if get_new_key() not in list_values:

            list_values.append(get_new_key())


def index_doc_new(doc_name, new_id):

    value = doc_new_index.get(get_new_key())

    if value == None:

        value = (doc_name, new_id)
        doc_new_index[get_new_key()] = value


def index_value_from_json(json_data, key, doc_name):

    for new in json_data:

        index_doc_new(doc_name, new[json_new_id])

        value = new[key]
        value = clean_text(value)
        value_list = value.split()

        for word in value_list:

            index_word(word)

        increase_new_pos_id()


def index_files_from_directory(directory):

    for doc_name in os.listdir(directory):

        json_data = get_json_data(directory + directory_path + doc_name)
        index_value_from_json(json_data, json_new_article, doc_name)

        reset_new_pos_in_doc()
        increase_doc_id()


def print_index(index):

    for item in index.items():

        print(item)


def save_index(index, doc_name):

    with open(doc_name, "wb") as fh:
        pickle.dump(index, fh)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="News directory")
    parser.add_argument("index", help="Index name")

    args = parser.parse_args()
    docs_directory = args.directory
    index_name = args.index

    index_files_from_directory(docs_directory)

    print_index(term_index)
    print_index(doc_new_index)

    save_index(term_index, index_name)
    save_index(doc_new_index, doc_new_index_save_name)
