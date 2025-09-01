"""
[입력]
ljes=njak

ddz=z=

nljj

c=c=

dz=ak

[출력]
6

3

3

4

3

"""

import sys

word = sys.stdin.readline().strip()
croatian_alph = ['dz=', 'lj', 'nj', 'c=', 'c-', 'd-', 's=', 'z=']

for char in croatian_alph:
    word = word.replace(char, 'a')

print(len(word))


"""
import sys

word = sys.stdin.readline().strip()
count = 0
i = 0

while i < len(word):
    if i + 2 < len(word) and word[i:i+3] == 'dz=':
        # 'dz='인 경우 (세 글자)
        count += 1
        i += 3
    elif i + 1 < len(word) and word[i:i+2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        # 두 글자 크로아티아 알파벳인 경우
        count += 1
        i += 2
    else:
        # 그 외 나머지 경우 (일반 알파벳)
        count += 1
        i += 1

print(count)

"""