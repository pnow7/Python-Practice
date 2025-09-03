"""
[입력]
3
happy
new
year

9
aaa
aaazbz
babb
aazz
azbz
aabbaa
abacc
aba
zzaz

[출력]
3

2
"""
import sys

N = int(sys.stdin.readline())
count = 0

for _ in range(N):
    alpha_check = [False] * 26
    word = sys.stdin.readline().strip()
    
    # 단어가 비어있거나 한 글자일 경우 그룹 단어로 처리
    if len(word) <= 1:
        count += 1
        continue
    
    is_group_word = True
    
    # 첫 번째 문자는 먼저 기록
    # ord() 함수는 문자를 아스키코드로 변환
    alpha_check[ord(word[0]) - ord('a')] = True
    
    # 두 번째 문자부터 끝까지 반복하면서 검사
    for i in range(1, len(word)):
        current_char = word[i]
        prev_char = word[i-1]
        
        # 현재 문자와 이전 문자가 다를 때
        if current_char != prev_char:

            # 현재 문자가 이전에 나온 적이 있는지 확인
            if alpha_check[ord(current_char) - ord('a')] == True:
                is_group_word = False
                break  # 그룹 단어가 아니므로 반복 중단
            
            else:
                # 처음 나온 문자이므로 기록
                alpha_check[ord(current_char) - ord('a')] = True
                
    if is_group_word:
        count += 1

print(count)