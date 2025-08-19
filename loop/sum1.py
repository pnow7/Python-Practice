# 값을 할당 하는 순간 자동으로 int 형으로 인식

n = int(input())

sum = 0

for i in range(1, n+1):
    sum += i

print(sum)