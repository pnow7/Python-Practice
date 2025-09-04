"""
corrcoef(x, y) 함수는 요소들의 상관관계를 계산
이때 x와 y는 데이터를 담고 있는 리스트나 배열이 될 수 있다.
"""
import numpy as np

x = [i for i in range(100)]
y = [i ** 2 for i in range(100)]
z = [ 100 * np.sin(3.14*i/100) for i in range(100) ]

print(x)
print(y)

# x와 x, y와 x
# y와 x, y와 y
corr = np.corrcoef(x, y)
print('\n', corr, '\n')

result = np.corrcoef([x, y, z])
print(result)



