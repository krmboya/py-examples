import sys

while True:
    in_str = sys.stdin.readline()
    if not in_str:
        break
    n, d = [int(i) for i in in_str.strip().split()]
    l_str = sys.stdin.readline()
    l = l_str.strip().split()
    if n != d:
        l = l[d:] + l[:d]
        l_str = " ".join(l) + "\n"
    sys.stdout.write(l_str)
