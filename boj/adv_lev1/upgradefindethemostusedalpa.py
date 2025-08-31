import sys
from collections import Counter

word = sys.stdin.readline().strip().upper()

# Counter로 각 문자의 빈도수를 한 번에 계산
count_dict = Counter(word)

if not count_dict:
    print('?')
else:
    max_value = max(count_dict.values())

    # 특정 조건을 만족하는 요소들만 모아서 새로운 리스트를 만드는 방식
    most_common_letters = [k for k, v in count_dict.items() if v == max_value]

    if len(most_common_letters) > 1:
        print('?')
    else:
        print(most_common_letters[0])

"""
[k for k, v in count_dict.items() if v == max_value]

BAAANANA라는 단어가 입력되면 
count_dict는 {'B': 1, 'A': 3, 'N': 2}가 되고
max_value는 3

('B', 1): 1 == 3 (거짓) -> 버림

('A', 3): 3 == 3 (참) -> k인 **'A'**를 리스트에 추가

('N', 2): 2 == 3 (거짓) -> 버림

* 대체문
most_common_letters = []
for k, v in count_dict.items():
    if v == max_value:
        most_common_letters.append(k)

"""