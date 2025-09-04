import numpy as np

# 난수를 발생시키는 초기값
np.random.seed(100)   

# np.random.rand(5): 0과 1 사이 균일한 분포에서 난수 5개 생성
print(np.random.rand(5).round(1) * 10,'\n')

# 2차원 array로 random 발생
print(np.random.rand(5, 3), '\n')

# 주사위 100번 시뮬레이션(# 1부터 6까지)
print(np.random.rand() * 6 + 1, '\n')    
print(int(np.random.rand() * 6 + 1), '\n')

# 10~20 사이 난수 발생
a = 10
b = 20
print(np.random.rand(5), '\n')
print((b - a) * np.random.rand(5) + a, '\n')

# 1~6 정수발생
print(np.random.randint(1, 7, size = 10), '\n')

# 1~10 사이의 정수 4x7 모양으로 발생
print(np.random.randint(1, 11, size = (4, 7)), '\n')