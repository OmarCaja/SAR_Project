import pickle

from constants.data_name_constants import WORDS_LIST_DATA, WORDS_TRIE_DATA
from constants.path_constants import SERIALIZED_OBJECTS_PATH


def save_words_list(words_list):
    with open(SERIALIZED_OBJECTS_PATH + WORDS_LIST_DATA, "wb") as handle:
        pickle.dump(words_list, handle, protocol=pickle.HIGHEST_PROTOCOL)


def save_words_trie(words_trie):
    with open(SERIALIZED_OBJECTS_PATH + WORDS_TRIE_DATA, "wb") as handle:
        pickle.dump(words_trie, handle, protocol=pickle.HIGHEST_PROTOCOL)


def save_news_index(index, index_name):
    with open(SERIALIZED_OBJECTS_PATH + index_name, "wb") as fh:
        pickle.dump(index, fh)


def import_words_list():
    with open(SERIALIZED_OBJECTS_PATH + WORDS_LIST_DATA, 'rb') as handle:
        words_list = pickle.load(handle)
        return words_list


def import_words_trie():
    with open(SERIALIZED_OBJECTS_PATH + WORDS_TRIE_DATA, 'rb') as handle:
        words_trie = pickle.load(handle)
        return words_trie


def import_news_index(index_name):
    with open(SERIALIZED_OBJECTS_PATH + index_name, 'rb') as handle:
        index = pickle.load(handle)
        return index
