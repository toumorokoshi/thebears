"""
Usage:
  thebears <dictionary> <required_chars> <priority_chars>...
"""
import pprint
import json
import sys
from .board import Board, InvalidChoice
from .dictionary import Dictionary
from docopt import docopt


def main(argv=sys.argv[1:]):
    arguments = docopt(__doc__, version='0.0.1')
    board = Board(arguments["<required_chars>"],
                  arguments["<priority_chars>"])
    with open(arguments["<dictionary>"]) as fh:
        dictionary = Dictionary(json.loads(fh.read()))

    word_with_score = []

    for word in dictionary.words:
        try:
            score = board.rank(word)
            word_with_score.append((score, word.raw))
        except InvalidChoice as e:
            continue

    pprint.pprint(list(reversed(sorted(word_with_score))))
