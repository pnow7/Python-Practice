import sys
from itertools import zip_longest

words = [sys.stdin.readline().strip() for _ in range(5)]
result = ''.join([''.join(x) for x in zip_longest(*words, fillvalue='')])

print(result)