import numpy as np

# 정규분포
# 평균 0, 표준편차 1인 표준정규분포
print(np.random.randn(10), '\n')

print(np.random.randn(5, 4), '\n')

# 평균(mean)
# 큰 수의 법칙: 시료 수가 많을 수록 평균이 0에 가까워짐 
print(np.mean(np.random.randn(10000000)), '\n')

# 표준편차
print(np.std(np.random.randn(10000000)), '\n')

# 평균: mu, 표준편차: sigma
mu = 170
sigma = 8

# 평균은 170, 표준편차는 8인 정규분포
random_height = mu + np.random.randn(100) * sigma
print(random_height, '\n')

# 평균(np.mean(~~), ~~.mean())
print(np.mean(random_height), '\n')
print(random_height.mean(), '\n')

# 중앙값
a = np.array([ 3, 7, 1, 2, 210]) 
print(np.median(a), '\n')

