"""
[입력]
472
385

[출력]
2360
3776
1416
181720
"""

# num1은 숫자, num2는 문자열

num1 = int(input())
num2 = input()

n3 = num1 * int(num2[2])
n4 = num1 * int(num2[1])
n5 = num1 * int(num2[0])

print(n3)
print(n4)
print(n5)
print(num1 * int(num2))