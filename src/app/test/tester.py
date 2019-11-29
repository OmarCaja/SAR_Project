import argparse

from data_structures.trie import trie
from read_data import reader

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="File name")

    args = parser.parse_args()
    file_name = args.file_name

    words_list = reader.get_words_list(file_name)
    word_set = set(words_list)
    words_list = list(word_set)

    trie = trie.trie()
    trie.index_words_list_in_trie(words_list)
