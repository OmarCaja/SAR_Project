from data_structures.trie.trie import trie
from words_distance.dynamic_programming.word_to_trie import levenshtein

tr = trie()
tr.addPalabra('hola')
tr.addPalabra('holo')
tr.addPalabra('hloa')
tr.addPalabra('aloh')
tr.addPalabra('holi')

levenshtein('hola', tr, 2)