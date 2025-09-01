import numpy as np

players = [[170, 76.4], 
           [183, 86.2], 
           [181, 78.5], 
           [176, 80.1]]

np_players = np.array(players)

# 키 180 이상
print(np_players[:, 0] >= 180, '\n')

# 몸무게 80 이상만(논리형 출력)
print(np_players[:, 1] > 80, '\n')

# 몸무게만 출력(값 출력)
print(np_players[np_players[:, 1] >= 80, 1], '\n')

# 키, 몸무게 같이 출력
print(np_players[np_players[:, 1] >= 80, :], '\n')

