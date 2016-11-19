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
    # Candidates are:
    # the word itself it appears in dictionary or
    # words 1 edit away if they appear in dictionary or
    # words 2 edits away if they appear in dictionary or
    # the word itself if none of the above check out
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])


def known(words):
    """Returns subset of `words` that appear in dictionary WORDS"""
    return set(w for w in words if w in WORDS)


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

    # Transpose the first, second character of the second word in each
    # tuple e.g. ['plepa', 'lepap']
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]

    # Replace the 1st character of the second word with each
    # letter of the alphabet e.g. 
    # ['pplea', 'ppleb', 'pplec' ... 'ppleap', 'pplebp', 'pplecp' .. etc
    
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]

    # Insert a letter of the alphabet between words in each tuple
    # e.g. ['ppleaa', 'ppleba', ... 'pleaap', 'pplebap' ...
    inserts = [L + c + R for L, R in splits for c in letters]

    # and now rid all the duplicates among the above lists
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    """All edits that are 2 edits away from `word`"""
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))



    




