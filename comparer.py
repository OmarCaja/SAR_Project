#!/usr/bin/python3

import argparse
from reader import get_word_list
from Damerau_Leveshtein import damerau_levenshtein


def compare_word_list(word_list):

    for word1 in word_list:

        print(word1)
        print(' ')

        for word2 in word_list:

            print(word2)
            print(' ')
            print(damerau_levenshtein(word1, word2))
        
        print('\n')


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="File name")

    args = parser.parse_args()
    file_name = args.file_name

    word_list = get_word_list(file_name)
    compare_word_list(word_list)
