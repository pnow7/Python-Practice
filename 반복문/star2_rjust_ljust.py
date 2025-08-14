import sys

n = int(sys.stdin.readline())

star = ""
for i in range(1, n+1):
    star += " " * (n - i)
    star += "*" * (i)
    print(star)
    star = ""

for i in range(1, n+1):
    print(('*' * i).rjust(n))

for i in range(1, n+1):
    print(('*' * i).ljust(n, '-'))

"""
import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    print(('*' * i).rjust(n))
"""