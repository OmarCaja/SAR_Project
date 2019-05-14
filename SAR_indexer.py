#!/usr/bin/python3

'''
Proyecto de Practicas: SAR indexer
Autores:
Omar Caja Garcia
Zhihao Zhang
Pablo Lopez Orrios
Jose Antonio Culla de Moya
'''

import sys
import os
import argparse
import pickle
import re
import json


doc_news_index = {}
news_counter = 1

article_index = {}
title_index = {}
keywords_index = {}
date_index = {}
summary_index = {}

json_keys_indexes = [('article', article_index), 
                     ('title', title_index), 
                     ('keywords', keywords_index), 
                     ('date', date_index), 
                     ('summary', summary_index)]

key_pos = 0
index_pos = 1

json_new_id = 'id'

clean_re = re.compile('\\W+')


def clean_text(text):

    return clean_re.sub(' ', text)


def lowercase_text(text):

    return text.lower()


def get_news_counter():

    return news_counter;


def increase_news_counter():

    global news_counter
    news_counter += 1


def get_new_key():

    return get_news_counter()


def get_json_data(doc_name):

    with open(doc_name, "r") as json_file:

        return json.load(json_file)


def index_word(word, index, pos):

    positionlist=[]
    index[word] = index.get(word, {})
    dict_values = (index.get(word))
    positionlist=dict_values.get(get_new_key(), positionlist)
    positionlist.append(pos)
    dict_values[get_new_key()] = dict_values.get(get_new_key(), positionlist)


def index_doc_new(file_path, new_id):

    value = doc_news_index.get(get_new_key())

    if value == None:

        value = (file_path, new_id)
        doc_news_index[get_new_key()] = value


def index_value_from_json(json_data, file_path):

    for new in json_data:

        index_doc_new(file_path, new[json_new_id])

        for key_index in json_keys_indexes:
            value = new[key_index[key_pos]]
            if key_index[index_pos]!=date_index:
                value = clean_text(value)
            value = lowercase_text(value)
            value_list = value.split()
            pos=0

            for word in value_list:
                index_word(word, key_index[index_pos],pos)
                pos=pos+1
                
    
        increase_news_counter()


def index_files_from_directory(directory):

    for subdir, dirs, files in os.walk(directory):

        for file in files:

            file_path = os.path.join(subdir, file)

            json_data = get_json_data(file_path)
            index_value_from_json(json_data, file_path)


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

    print_index(article_index)
    print_index(title_index)
    print_index(keywords_index)
    print_index(date_index)
    print_index(summary_index)
    print_index(doc_news_index)
    
    save_index((article_index, title_index, keywords_index, date_index, summary_index, doc_news_index), index_name)
