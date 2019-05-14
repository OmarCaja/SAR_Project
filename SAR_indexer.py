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

term_index = {}
doc_new_index = {}
date_index = {}
summary_index = {}
title_index = {}
keywords_index = {}

doc_new_index_save_name = 'doc_new_index'

doc_id = 0
new_pos_in_doc = 0
doc_id_news_id_separator = '_'

json_new_article = 'article'
json_new_id = 'id'
json_new_title= 'title'
json_new_summary= 'summary'
json_new_keywords= 'keywords'
json_new_date= 'date'

clean_re = re.compile('\\W+')


def clean_text(text):

    return clean_re.sub(' ', text)


def lowercase_text(text):

    return text.lower()


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
    new_pos_in_doc = 0


def get_new_key():

    return str(get_doc_id()) + doc_id_news_id_separator + str(get_new_pos_in_doc())


def get_json_data(doc_name):

    with open(doc_name, "r") as json_file:

        return json.load(json_file)


def index_word_values(word):

    dict_values = term_index.get(word)

    if dict_values == None:

        dict_values = {}

        term_index[word] = dict_values

    if dict_values.get(get_new_key(), 0) == 0:

        dict_values[get_new_key()] = 1

    else:

        dict_values[get_new_key()] = dict_values.get(get_new_key()) + 1 

def index_word_summary(word):
    
    dict_values = summary_index.get(word)

    if dict_values == None:

        dict_values = {}

        summary_index[word] = dict_values

    if dict_values.get(get_new_key(), 0) == 0:

        dict_values[get_new_key()] = 1

    else:

        dict_values[get_new_key()] = dict_values.get(get_new_key()) + 1 
   

def index_word_keywords(word):
    
    dict_values = keywords_index.get(word)

    if dict_values == None:

        dict_values = {}

        keywords_index[word] = dict_values

    if dict_values.get(get_new_key(), 0) == 0:

        dict_values[get_new_key()] = 1

    else:

        dict_values[get_new_key()] = dict_values.get(get_new_key()) + 1 
        
        
def index_word_title(word):
    
    dict_values = title_index.get(word)

    if dict_values == None:

        dict_values = {}

        title_index[word] = dict_values

    if dict_values.get(get_new_key(), 0) == 0:

        dict_values[get_new_key()] = 1

    else:

        dict_values[get_new_key()] = dict_values.get(get_new_key()) + 1 
    
def index_word_date(word):
    
    dict_values = date_index.get(word)

    if dict_values == None:

        dict_values = {}

        date_index[word] = dict_values

    if dict_values.get(get_new_key(), 0) == 0:

        dict_values[get_new_key()] = 1

    else:

        dict_values[get_new_key()] = dict_values.get(get_new_key()) + 1    
    


def index_doc_new(file_path, new_id):

    value = doc_new_index.get(get_new_key())

    if value == None:

        value = (file_path, new_id)
        doc_new_index[get_new_key()] = value


def index_value_from_json(json_data, key, file_path):

    for new in json_data:

        index_doc_new(file_path, new[json_new_id])
        value = new[key]
        value = clean_text(value)
        value = lowercase_text(value)
        value_list = value.split()
        for word in value_list:
            if key==json_new_article:
                index_word_values(word)
            if key==json_new_title:
                index_word_title(word)
            if key==json_new_keywords:
                index_word_keywords(word)
            if key==json_new_summary:
                index_word_summary(word)
            if key==json_new_date:
                index_word_date(word)


        increase_new_pos_id()


def index_files_from_directory(directory):

    for subdir, dirs, files in os.walk(directory):

        for file in files:

            file_path = os.path.join(subdir, file)

            json_data = get_json_data(file_path)
            index_value_from_json(json_data, json_new_article, file_path)
            index_value_from_json(json_data, json_new_title, file_path)
            index_value_from_json(json_data, json_new_summary, file_path)
            index_value_from_json(json_data, json_new_keywords, file_path)
            index_value_from_json(json_data, json_new_date, file_path)

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

    """print_index(term_index)
    print_index(doc_new_index)
    print_index(title_index)
    print_index(summary_index)
    print_index(keywords_index)
    print_index(date_index)"""
    
    
    save_index((term_index, doc_new_index), index_name)
