"""
Each input line i in no_lines:
 - read in the input line of brackets
 - write YES/NO to stdout, whether the brackets are balanced or not
"""
import sys

matches = {
    "(": ")",
    "{": "}",
    "[": "]"
}

stack = []

def push_or_pop(bracket):

    if len(stack) and matches.get(stack[-1]) == bracket:
        stack.pop()
    else:
        stack.append(bracket)


no_lines = int(sys.stdin.readline().strip())

for i in xrange(no_lines):
    brackets = sys.stdin.readline().strip()
    for b in brackets:
        push_or_pop(b)
    output = "NO" if len(stack) else "YES"
    sys.stdout.write(output + "\n")
    stack = []
