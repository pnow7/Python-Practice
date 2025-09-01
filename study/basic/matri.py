matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for row in matrix:
    for i in range(len(row)):
        print(row[i], end = '')

        if i <len(row) -1:
            print(',', end = '')
    print()

print()

rows = 5
cols = 3
my_array = [[0] * cols for _ in range(rows)]

print(my_array)