"""
UNUCIC는 868242와 같다.

숫자마다 +2

[입력]
WA

UNUCIC

[출력]
13

36
"""

import sys

word = sys.stdin.readline().strip()

time = 0

for char in word:
    if 'A' <= char <= 'C':
        time += 3  
    elif 'D' <= char <= 'F':
        time += 4  
    elif 'G' <= char <= 'I':
        time += 5  
    elif 'J' <= char <= 'L':
        time += 6
    elif 'M' <= char <= 'O':
        time += 7
    elif 'P' <= char <= 'S':
        time += 8  
    elif 'T' <= char <= 'V':
        time += 9
    elif 'W' <= char <= 'Z':
        time += 10 

print(time)

"""
import sys

dial = {
    'A': 2, 'B': 2, 'C': 2,
    'D': 3, 'E': 3, 'F': 3,
    'G': 4, 'H': 4, 'I': 4,
    'J': 5, 'K': 5, 'L': 5,
    'M': 6, 'N': 6, 'O': 6,
    'P': 7, 'Q': 7, 'R': 7, 'S': 7,
    'T': 8, 'U': 8, 'V': 8,
    'W': 9, 'X': 9, 'Y': 9, 'Z': 9
}

word = sys.stdin.readline().strip()

for char in word:
    time += dial[char] + 1

print(time)

"""