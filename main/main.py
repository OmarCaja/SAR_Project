import argparse

from data_structures.data_structures import save_words_list, save_words_trie
from data_structures.trie import trie
from read_data.reader import get_words_list

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="File name")

    args = parser.parse_args()
    file_name = args.file_name

    words_list = get_words_list(file_name)
    save_words_list(words_list)

    trie = trie.trie()
    trie.index_words_list_in_trie(words_list)
    save_words_trie(trie)
