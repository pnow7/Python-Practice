"""
- numpy를 사용하는 이유
1) 메모리를 적게 차지하고 list보다 속도가 빠름
2) 배열 간에 수학적인 벡터 연산 가능
3) 고급 연산자와 풍부한 함수 제공
"""

import numpy as np

mid_scores = [10, 20, 30]
final_scores = [70, 80, 90]

print(mid_scores + final_scores)

total = []
for i in range(len(mid_scores)):
    total.append(mid_scores[i] + final_scores[i])

print(total)
print('*' * 10, "numpy 사용하기", '*' * 10)

# np.array 사용
mid_scores = np.array(mid_scores)
final_scores = np.array(final_scores)

print(f"점수 합: {mid_scores + final_scores}")
print(f"점수 평균: {(mid_scores + final_scores) // 2}")

# range도 사용 가능
a = np.array(range(1, 11))
b = np.array(range(10, 101, 10))

print(a + b, a - b, a * b, a / b)