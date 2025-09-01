"""
[입력]
pulljima

[출력]
8

** strip() 을 써줘야 하는 이유 **
sys.stdin.readline() 만 쓰면 pulljima/n에서 '/n' 까지 읽어오기때문에
strip()으로 개행된 문자는 제거해야함

"""

import sys

word = sys.stdin.readline().strip()

print(len(word))