import copy

original = [[1, 2, 3], [4, 5, 6]]

# 얕은 복사
shallow = copy.copy(original)

# 깊은 복사
deep = copy.deepcopy(original)

print("원본:", original)
print("얕은 복사:", shallow)
print("깊은 복사:", deep)

original[0][0] = 99

print("\n---수정후---")
print("원본:", original)
print("얕은 복사:", shallow)
print("깊은 복사:", deep)