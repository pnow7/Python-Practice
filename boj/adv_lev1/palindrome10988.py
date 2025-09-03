"""
[입력]
level

baekjoon

[출력]
1

0
"""

import sys

word = list(sys.stdin.readline().strip())

if len(word) % 2 != 0:
    word.remove(word[len(word) // 2])

reversed_word = list(reversed(word))

# print(word, reversed_word)

if word == reversed_word:
    print(1)
else:
    print(0)









