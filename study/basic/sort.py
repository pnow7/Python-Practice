a = [10, 5, 20, 30]
a.sort()
print(a)

b = [1, 5, 1, 23, 4]
print(sorted(b))

c = [38, 21, 53, 62, 19]
for index, value in enumerate(c):
    print(index, value, sep= ' - ')
    
d = [213, 13, 15, 985, 84]
for i in range(0, len(d)):
    print(d.index(d[i]),  d[i], sep = ' * ')