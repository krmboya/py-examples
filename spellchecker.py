# Annotated spell checker as describe by Peter Norvig: http://norvig.com/spell-correct.html
import re
import string
from collections import Counter

# dict_file = "/etc/dictionaries-common/words" - I think we need many occurrences of the same word
dict_file = "big.txt"


def words(text): return re.findall(r'\w+', text.lower())  # return all words in text


WORDS = Counter(words(open(dict_file).read()))


def P(word, N=sum(WORDS.values())):
    """Probability of `word`"""
    return WORDS[word] / N


def correction(word):
    """Most probable correction of `word`"""
    return max(candidates(word), key=P)  # candidate with highest probability


def candidates(word):
    "Generate possible corrections for `word`"
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    """Returns subset of `words` that appear in dictionary WORDS"""
    return set(w for w in words in w in WORDS)


def edits1(word):  # probably most interesting part
    """All edits that are 1 edit away from word"""

    letters = string.lowercase

    # list of tuples where the second word in each tuple consists of letters
    # shifted off from the first word in an incrementing fashion
    # e.g [('apple', ''), ('pple', 'a'), ('ple', 'ap'), ('le', 'app'),
    #      ('e', 'appl'), ('', 'apple')]
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]

    # concatenate each tuple after deleting 1st char of second
    # using previous example, deletes will be
    # ['apple', 'pple', 'plep', lepp']
    deletes = [L + R[1:] for L, R in splits if R]

    transposes = # will continue here..
    



    




