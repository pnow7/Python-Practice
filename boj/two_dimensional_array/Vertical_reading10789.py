"""
[입력]
ABCDE
abcde
01234
FGHIJ
fghij

[출력]
Aa0FfBb1GgCc2HhDd3IiEe4Jj
"""

import sys

word = [ list(sys.stdin.readline().strip()) for _ in range(5) ]

result_string = ""

# 세로로 읽기 때문에 i, j 반대로
for j in range(15):
    for i in range(5):
        if len(word[i]) > j:
            result_string += word[i][j] 

print(result_string)


"""
import sys

words = [sys.stdin.readline().strip() for _ in range(5)]
max_len = max(len(word) for word in words)

result = ''.join([words[i][j] for j in range(max_len) for i in range(5) if len(words[i]) > j])

print(result)
"""