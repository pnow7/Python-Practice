# M 은 최댓값
# 모든 점수를 점수/M * 100으로 고침
# 그 중 가장 큰 숫자를 출력

"""
[입력]
3
40 80 60

3
10 20 30

[출력]
75.0

66.666667
"""

import sys

N = int(sys.stdin.readline())

score = list(map(int, sys.stdin.readline().split()))

score_max = max(score)
score_average = (sum(score) / N * 100) / score_max

print(score_average)