c = list(range(10, 4, -1))
print(c)

c.append('응 아니야')
print(c)

c.append([1,2])
print(c)

# 0번재 리스트에 삽입
c.insert(0, '0번째 삽입')
print(c)

# 맨끝에 리스트 추가
c.extend(['맨끝', '이걸삽입', 1])
print(c)

# 0번재 인덱스 삭제
c.remove(c[0])
print(c)

# append랑 extend 차이
# list1 = [1, 2, 3]
# list2 = [4, 5]

# append: 출력 -> [1, 2, 3, [4, 5]]
# extend: 출력 -> [1, 2, 3, 4, 5]