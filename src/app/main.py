import argparse

from data_structures import data_structures_handler
from data_structures.trie import trie
from read_data import reader

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="File name")

    args = parser.parse_args()
    file_path = args.file_path

    words_list = reader.get_words_list(file_path)
    word_set = set(words_list)
    words_list = list(word_set)
    data_structures_handler.save_words_list(words_list)

    trie = trie.trie()
    trie.index_words_list_in_trie(words_list)
    data_structures_handler.save_words_trie(trie)
