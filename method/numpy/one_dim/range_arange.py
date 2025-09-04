"""
- range() 함수와 arange() 함수 비교

1) np.arange( [start], stop, [step] )
2) range()와 비슷하지만 arange()는 numpy 배열을 만듬
"""

import numpy as np

print(np.arange(10), '\n')
print(np.arange(1, 6), '\n')
print(np.arange(1, 10, 2), '\n')

# 주의: range와 결정적 차이 -> range는 정수만 가능
# print(range(1, 10, 2.5)) Error
print(np.arange(1, 10, 2.5), '\n')