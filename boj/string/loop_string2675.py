"""
[입력]
2
3 ABC
5 /HTP

[출력]
AAABBBCCC
/////HHHHHTTTTTPPPPP
"""

import sys

T = int(sys.stdin.readline())

result = []

for _ in range(T):
    R, word = sys.stdin.readline().split()
    R = int(R)

    #for char in word:
        #print(char * R, end="")
    #print()

    new_word =""
    for char in word:
        new_word += char * R
    
    result.append(new_word)

print('\n'.join(result))

                  

