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

croatian_alph = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = list(sys.stdin.readline().split())

count = 0

for items in word:
    if items in croatian_alph:
        count += 1



print(count)