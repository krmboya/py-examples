import  sys

"""
Input:

1st line: m and n representing no of words in magazine, ransom not respectively
2nd line: m separated words represeting words in magazine
3rd line: n separatd words representing words in ransom note

Output:
Yes/No - whether there enough words in mag matching all in ransom note (case-sensitive)
"""

m, n = [int(i) for i in sys.stdin.readline().strip().split()]
m_words = [w for w in sys.stdin.readline().strip().split()]
n_words = [w for w in sys.stdin.readline().strip().split()]

n_words_count, m_words_count = {}, {}

for w in n_words:
    n_words_count[w] = n_words_count.get(w, 0) + 1

for w in m_words:
    m_words_count[w] = m_words_count.get(w, 0) + 1
    

output = "Yes" if all([
    n_words_count[w] == m_words_count[w] if w in m_words_count else False 
    for w in n_words_count
]) else "No"

sys.stdout.write(output + "\n")


