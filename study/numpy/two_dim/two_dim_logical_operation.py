import numpy as np

np_array = np.arange(1, 10).reshape(3, 3)

print(np_array, '\n')
print(np_array > 5, '\n')
print(np_array % 2 == 0, '\n')

# 요소 출력
print(np_array[np_array > 5], '\n')
print(np_array[np_array % 2 == 0], '\n')

# 세번째 열 원소 출력
print(np_array[:, 2], '\n')