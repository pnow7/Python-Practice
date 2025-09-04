import numpy as np

ages = np.array([18, 19, 25, 30, 28])

# 논리형 반환
print(ages >= 20)

# 값 반환(where)
result_array = np.where(ages >= 20, ages, 0)
print(result_array)

# 값 반환 편하게 하는 방법
print(ages[ages >= 20])