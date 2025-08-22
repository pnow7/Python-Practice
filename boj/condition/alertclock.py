# print(a, b) 여러 개의 값을 쉼표로 구분하여 출력하면 값 사이에 기본적으로 공백 자동 추가
# print(a, b, sep=':') 값 사이 : 추가 

hour, min = map(int, input().split())

if min >= 45:
    min -= 45
    print(hour, min)
else:
    hour -= 1
    min += 15
    print(hour, min)