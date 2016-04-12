from collections import defaultdict


class Dictionary:

    def __init__(self, dictionary):
        self._words = [
            Word(w) for w in dictionary.keys()
        ]

    @property
    def words(self):
        return self._words


class Word:

    def __init__(self, word):
        word = word.lower()
        self._raw = word
        self._frequencies = defaultdict(int)
        for c in word:
            self._frequencies[c] += 1

    @property
    def frequencies(self):
        return self._frequencies

    @property
    def raw(self):
        return self._raw
