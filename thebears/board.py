import copy


class InvalidChoice(Exception):
    pass


class Board:

    def __init__(self, required_chars, priority_char_list):
        self._required_chars = required_chars
        self._priority_char_list = priority_char_list

    def rank(self, word):
        """ return a rank of the value of the word """
        frequencies = copy.deepcopy(word.frequencies)
        for required_char in self._required_chars:
            frequencies[required_char] -= 1
            if frequencies[required_char] < 0:
                raise InvalidChoice("required characters not completely used for {0}".format(
                    word.raw
                ))
        score = 0
        if all(f == 0 for f in frequencies.values()):
            return 0
        priority_score = len(self._priority_char_list)
        for char_list in self._priority_char_list:
            for c in char_list:
                if frequencies[c] == 0:
                    continue
                frequencies[c] -= 1
                score += priority_score
                if all(f == 0 for f in frequencies.values()):
                    return score
            priority_score -= 1

        raise InvalidChoice("unused characters in the word for {0}".format(
            word.raw
        ))
