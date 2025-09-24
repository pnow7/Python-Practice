import numpy as np

scores = np.array([88, 72, 93, 94, 89, 78, 99])

print(scores[2], scores[-1])

# - 주의
print(scores[:3], scores[:-3])

print(scores[3:-1])
