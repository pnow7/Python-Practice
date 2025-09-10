import sys

N, M = map(int, sys.stdin.readline().split())

# [ ] 안에 list 라서 2차원 행렬
arr1 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
arr2 = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# zip 함수와 리스트 컴프리헨션을 활용한 덧셈
arr3 = [[arr1[i][j] + arr2[i][j] for j in range(M)] for i in range(N)]

for row in arr3:
    print(*row)