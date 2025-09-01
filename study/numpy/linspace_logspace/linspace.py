"""
- linspace(linear: 선형적)

1) np.linspace(start, stop, num = 50)
start: 데이터 생성을 시작할 값(생략 불가)
stop: 데이터 생성을 멈출 값으로 생략할 수 없음, 데이터는 stop까지 생성(stop -1 아님)
num: 데이터 생성 개수(기본값은 50개)
"""

import numpy as np

# 0부터 10까지 50개 실수 데이터 생성
print(np.linspace(0, 10), '\n')

# 0부터 10까지 11개 데이터 생성
print(np.linspace(0, 10, 11), '\n')

# endpoint 포함 -> True
# endpoint 포함X -> False
print(np.linspace(0, 10, 10, endpoint = True))
print(np.linspace(0, 10, 10, endpoint = False))