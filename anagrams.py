"""
Input: 2 lines for each string
Output: Min no of characters to delete for strings to be anagrams
"""
import sys
import string

letters = string.lowercase

f = lambda x, y: len([c for c in y if c == x])

g = lambda x, y: (x - y) if x > y else (y - x)


while True:
    to_del = 0
    a = sys.stdin.readline()
    if not a:
        break
    b = sys.stdin.readline()
    a, b = a.strip(), b.strip()
    for l in letters:
        a_count = f(l, a)
        b_count = f(l, b)
        to_del += g(a_count, b_count)
    output = "{0}\n".format(to_del)
    sys.stdout.write(output)
    
    
