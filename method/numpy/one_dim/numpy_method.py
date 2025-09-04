import numpy as np

a = np.array(range(1, 11))
b = np.array(range(10, 101, 10))

# a 객체의 형태 (shape) -> 1차원이라서 ,(쉼표) 뒤에 숫자가 나오지 않음
print(a.shape)

# 차원
print(a.ndim)

# a 객체의 내부 자료형
print(a.dtype)

# a 객체 내부 자료형이 차지하는 메모리 크기 (64bit) 64/8 -> 8비트
print(a.itemsize)

# a 객체 전체 항목 수
print(a.size)