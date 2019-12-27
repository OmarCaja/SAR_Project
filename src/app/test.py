import argparse
import time
from math import sqrt
from data_structures.trie import trie
from read_data import reader
from words_distance.dynamic_programming.word_to_word import levenshtein as levenshteinwtw
from words_distance.dynamic_programming.word_to_word import damerau_levenshtein as damerau_levenshteinwtw
from words_distance.dynamic_programming.word_to_trie import levenshtein as dynlevenshteinwtt
from words_distance.dynamic_programming.word_to_trie import damerau_levenshtein as dyndamerau_levenshteinwtt
from words_distance.branch_and_bound.word_to_trie import levenshtein as ramificacion
from words_distance.branch_and_bound.word_to_trie import damerau_levenshtein as ramificacion_damerau


def media(lista):
    return sum(lista) / len(lista)

def varianza(lista):
    s = 0
    m = media(lista)
    for elemento in lista:
        s += (elemento - m) ** 2
    return s / float(len(lista))

def desviacion_tipica(lista):
    return sqrt(varianza(lista))

def levenshteinwordtoword(F, F2, words_list):
    timelist=[]
    for i in range(1,20):
        time1 = time.time()
        for word in words_list:
            if (levenshteinwtw("casa", word) <= int(tolerancia)):
                F.write(word)
                F.write(str(levenshteinwtw("casa", word)))
                F.write("\n")
        time2 = time.time()
        F = open("basura.txt", "w", encoding='utf-8')
        timelist.append(time2 - time1)
    F2.write("\nMedia de tiempo:")
    F2.write(str(media(timelist)))
    F2.write("\nDesviacion tipica de tiempo: ")
    F2.write(str(desviacion_tipica(timelist)))
    timelist


def damerau_levenshteinwordtoword(F, F2, words_list):
    timelist = []
    for i in range(1,20):
        time1 = time.time()
        for word in words_list:
            if (levenshteinwtw("casa", word) <= int(tolerancia)):
                F.write(word)
                F.write(" ")
                F.write(str(damerau_levenshteinwtw("casa", word)))
                F.write("\n")
        time2 = time.time()
        F = open("basura.txt", "w")
        timelist.append(time2 - time1)
    F2.write("\nMedia de tiempo: ")
    F2.write(str(media(timelist)))
    F2.write("\nDesviacion tipica de tiempo: ")
    F2.write(str(desviacion_tipica(timelist)))


def dynamiclevenshteintrie(F, F2, trie, tolerancia):
    timelist = []
    for i in range(1,20):
        time1 = time.time()
        F.write(str(dynlevenshteinwtt("casa", trie, tolerancia)))
        time2 = time.time()
        F = open("basura.txt", "w")
        timelist.append(time2 - time1)
    F2.write("\nMedia de tiempo: ")
    F2.write(str(media(timelist)))
    F2.write("\nDesviacion tipica de tiempo: ")
    F2.write(str(desviacion_tipica(timelist)))


def dynamicdameraulevenshteintrie(F, F2, trie, tolerancia):
    timelist = []
    for i in range(1,20):
        time1 = time.time()
        F.write(str(dyndamerau_levenshteinwtt("casa", trie, tolerancia)))
        time2 = time.time()
        F = open("basura.txt", "w")
        timelist.append(time2 - time1)
    F2.write("\nMedia de tiempo: ")
    F2.write(str(media(timelist)))
    F2.write("\nDesviacion tipica de tiempo: ")
    F2.write(str(desviacion_tipica(timelist)))


def ramificacionlevenshteintrie(F, F2, trie , tolerancia):
    timelist = []
    for i in range(1,20):
        time1 = time.time()
        F.write(str(ramificacion("casa", trie, tolerancia)))
        time2 = time.time()
        F = open("basura.txt", "w")
        timelist.append(time2 - time1)
    F2.write("\nMedia de tiempo: ")
    F2.write(str(media(timelist)))
    F2.write("\nDesviacion tipica de tiempo: ")
    F2.write(str(desviacion_tipica(timelist)))


def ramificaciondameraulevenshteintrie(F, F2, trie, tolerancia):
    timelist = []
    for i in range(1,20):
        time1 = time.time()
        F.write(str(ramificacion_damerau("casa", trie, tolerancia)))
        time2 = time.time()
        F = open("basura.txt", "w")
        timelist.append(time2 - time1)
    F2.write("\nMedia de tiempo: ")
    F2.write(str(media(timelist)))
    F2.write("\nDesviacion tipica de tiempo: ")
    F2.write(str(desviacion_tipica(timelist)))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", help="File name")
    parser.add_argument("tolerancia", help="Tolerancia")

    args = parser.parse_args()
    file_name = args.file_name
    tolerancia = args.tolerancia

    words_list = reader.get_words_list(file_name)
    word_set = set(words_list)
    words_list = list(word_set)

    Fresult = open("resultlev.txt", "w", encoding='utf-8')
    Fresultdamerau = open("resultdam.txt", "w", encoding='utf-8')
    Fresultdyn = open("resultdynlev.txt", "w", encoding='utf-8')
    Fresultdyndamerau = open("resultdynda,.txt", "w", encoding='utf-8')
    Fresultram = open("resultramlev.txt", "w", encoding='utf-8')
    Fresultramdamerau = open("resultramdam.txt", "w", encoding='utf-8')
    Ftime = open("time.txt", "w")
    Ftime.write("tiempos de Levenshtein")
    levenshteinwordtoword(Fresult, Ftime, words_list)
    Ftime.write("\ntiempos de Damerau-Levenshtein")
    damerau_levenshteinwordtoword(Fresultdamerau, Ftime, words_list)


    trie = trie.trie()
    trie.index_words_list_in_trie(words_list)
    Ftime.write("\ntiempos de Levenshtein con programacion dinamica")
    dynamiclevenshteintrie(Fresultdyn, Ftime, trie, int(args.tolerancia))
    Ftime.write("\ntiempos de Damerau-Levenshtein con programacion dinamica")
    dynamicdameraulevenshteintrie(Fresultdyndamerau, Ftime, trie, int(args.tolerancia))
    Ftime.write("\ntiempos de Levenshtein con ramificacion")
    ramificacionlevenshteintrie(Fresultram, Ftime, trie, int(args.tolerancia))
    Ftime.write("\ntiempos de Damerau-Levenshtein con ramificacion")
    ramificaciondameraulevenshteintrie(Fresultramdamerau, Ftime, trie, int(args.tolerancia))