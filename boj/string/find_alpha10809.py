"""
[입력]
baekjoon

[출력]
1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
"""

import sys

result = [-1] * (26)

word = sys.stdin.readline().strip()

order = 0

for i in range(0, len(word)):
    order = ord(word[i]) - 97
    #order = ord(word[i]) - ord('a')
    
    if result[order] == -1:
        result[order] = i

print(*result)