from words_distance.dynamic_programming.damerau_leveshtein import damerau_levenshtein


def compare_word_list(word_list, searched_word, max_dist):
    word_distance_list = _make_word_distance_list(max_dist)

    for word in word_list:
        dist = damerau_levenshtein(searched_word, word)
        if dist <= max_dist:
            word_distance_list[dist].add((str(dist) + ':' + word))


def _make_word_distance_list(max_dist):
    word_distance_list = []

    for pos in range(max_dist + 1):
        word_distance_list.append(set())

    return word_distance_list
