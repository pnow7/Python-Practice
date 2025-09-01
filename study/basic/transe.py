# a -> 1, e -> 2 ..

table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))
