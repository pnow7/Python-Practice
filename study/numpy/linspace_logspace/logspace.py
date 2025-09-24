"""
- log 함수

1) np.logspace(start, stop, num = 50)
start: 10의 start승 부터 시작
stop: 데이터 생성을 멈출 값으로 생략할 수 없음, 데이터는 10의 stop승까지 생성
num: 기본값 50개
"""

import numpy as np

# 0부터 5까지 5개 값, 5는 포함 X
lin_s = np.linspace(0, 5, 5, endpoint = False)

# 10의 0승 부터 10의 5승까지 5개 값, 5는 포함 X
log_s = np.logspace(0, 5, 5, endpoint = False)
print(log_s, '\n')

# logspace와 똑같이 출력
print(10 ** lin_s, '\n')
