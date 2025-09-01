x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
d = {}

# key 
for i in x:
    print(i)

# 키, 값 같이
for key, value in x.items():
    print(key, value)

# 키, 값 뒤집기
for keys, values in x.items():
    d[values] = keys
print(d)