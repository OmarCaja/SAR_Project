import argparse

from read_data.reader import get_words_list
from words_distance.dynamic_programming.damerau_leveshtein import damerau_levenshtein


def compare_word_list(word_list, searched_word, max_dist):
    word_distance_list = make_word_distance_list(max_dist)

    for word in word_list:
        dist = damerau_levenshtein(searched_word, word)
        if dist <= max_dist:
            word_distance_list[dist].add((str(dist) + ':' + word))


def make_word_distance_list(max_dist):
    word_distance_list = []

    for pos in range(max_dist + 1):
        word_distance_list.append(set())

    return word_distance_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="File name")
    parser.add_argument("word_and_distance", help="Word for comparing and max distance")

    args = parser.parse_args()
    file_name = args.file_name
    searched_word = args.word_and_distance

    word_list = get_words_list(file_name)
    compare_word_list(word_list, searched_word, 3)
