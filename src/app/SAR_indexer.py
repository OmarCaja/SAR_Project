'''
Proyecto de Practicas: SAR indexer

Autores:

Omar Caja Garcia
Zhihao Zhang
Pablo Lopez Orrios
Jose Antonio Culla de Moya

Ampliaciones:

query con parentesis
multiples indices
ordenacion de los resultados
busqueda de terminos consecutivos
'''

import argparse
import os

from constants.path_constants import NEWS_PATH
from data_structures.data_structures_handler import save_news_index
from data_structures.trie.trie import trie
from read_data.reader import get_json_data, clean_text

doc_news_index = {}
news_counter = 1

article_index = {}
title_index = {}
keywords_index = {}
date_index = {}
summary_index = {}

article_trie = trie()
title_trie = trie()
keywords_trie = trie()
date_trie = trie()
summary_trie = trie()

json_keys_indexes = [('article', (article_index, article_trie)),
                     ('title', (title_index, title_trie)),
                     ('keywords', (keywords_index, keywords_trie)),
                     ('date', (date_index, date_trie)),
                     ('summary', (summary_index, summary_trie))]

key_pos = 0
index_pos = 1
date_pos = 3
counter_pos = 0
position_pos = 1

json_new_id = 'id'


def lowercase_text(text):
    return text.lower()


def get_news_counter():
    return news_counter


def increase_news_counter():
    global news_counter
    news_counter += 1


def get_new_key():
    return get_news_counter()


def index_word(word, index, pos):
    dict_values = index.get(word)

    if dict_values == None:
        dict_values = {}

        index[word] = dict_values

    if dict_values.get(get_new_key(), 0) == 0:

        dict_values[get_new_key()] = [1, [pos]]

    else:

        dict_values[get_new_key()][counter_pos] = dict_values.get(
            get_new_key())[0] + 1
        dict_values[get_new_key()][position_pos].append(pos)


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

            if key_index[key_pos] != json_keys_indexes[date_pos][key_pos]:
                value = clean_text(value)

            value = lowercase_text(value)
            value_list = value.split()

            word_position = 1

            for word in value_list:
                index, particular_trie = key_index[index_pos]
                index_word(word, index, word_position)
                particular_trie.addPalabra(word)
                word_position = word_position + 1

        increase_news_counter()


def index_files_from_directory(directory):
    for subdir, _, files in os.walk(directory):

        for file in files:
            file_path = os.path.join(subdir, file)

            json_data = get_json_data(file_path)
            index_value_from_json(json_data, file_path)


def print_index(index):
    for item in index.items():
        print(item)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", help="News directory")
    parser.add_argument("index", help="Index name")

    args = parser.parse_args()
    docs_directory = args.directory
    index_name = args.index

    index_files_from_directory(NEWS_PATH + docs_directory)

    save_news_index((article_index, title_index, keywords_index,
                     date_index, summary_index, doc_news_index), index_name)

    save_news_index((article_trie, title_trie, keywords_trie, date_trie, summary_trie), index_name + '_trie')
