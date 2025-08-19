n = int(input())

count = n // 4

result = []

for i in range(1, count+1):
    result.append("long")

results = " ".join(result)

print(f"{results} int")

"""
n = int(input())
count = n // 4

result = ""

for i in range(count):
    result += "long "

print(f"{result}int")

#####################

n = int(input())
count = n // 4

result = "long " * count

print(f"{result}int")
"""