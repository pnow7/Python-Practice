import numpy as np

# 1부터 11까지 numpy 형식 배열 생성
y = np.arange(12)
print(y, '\n')

# -1 넣으면 알아서 자동으로 3이 들어감
y2 = y.reshape(4, -1)
print(y2, '\n')

# 마찬가지로 똑같이 적용
print(np.arange(10).reshape(-1, 5), '\n')