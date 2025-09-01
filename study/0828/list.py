c = list(range(10, 4, -1))
print(c)

c.append('응 아니야')
print(c)

c.append([1,2])
print(c)

# 0번재 리스트에 삽입
c.insert(0, '0번째 삽입')
c.insert(1, '1번째 삽입')
print(c)

# 맨끝에 리스트 추가
c.extend(['맨끝', '삽입', 1])
print(c)

# 0번재 인덱스 삭제
c.remove(c[0])
print(c)

# 1번째 인덱스 삭제
# (remove로 0번째 인덱스 삭제돼서 앞으로 땡겨져옴)
del c[0]
del c[1]
print(c)

print('**' * 20)

# append()
list_append = ['a', 'b']
list_append.append('cd')
print(list_append)  # ['a', 'b', 'cd']

# extend()
list_extend = ['a', 'b']
list_extend.extend('cd')
print(list_extend)  # ['a', 'b', 'c', 'd']

# append랑 extend 차이
# list1 = [1, 2, 3]
# list2 = [4, 5]

# append: 출력 -> [1, 2, 3, [4, 5]]
# extend: 출력 -> [1, 2, 3, 4, 5]