"""
[입력]
60466175 36

[출력]
ZZZZZ

"""

import sys
import string

alpa_dict = {
    char: ord(char) - 55 for char in string.ascii_uppercase
}

N, B = map(int ,sys.stdin.readline().split())

result = []

while True:
    quotient = N // B
    remainder = N % B
    
