def process_info(name, *args, **kwargs):
    print(f"이름: {name}")
    print(f"(*튜플): {args}")
    print(f"(**딕셔너리): {kwargs}")
    print("-" * 20)

# 1. 위치 인자와 키워드 인자를 모두 전달
process_info('김철수', '학생', 25, city='서울', job='개발자')

# 2. 위치 인자만 전달
process_info('박영희', '회사원', 30)

# 3. 키워드 인자만 전달
process_info('이민지', city='부산', hobby='여행')

# * 1개: 키만 반환
# ** 2개: 키와 값을 합쳐서 반환
# 출력이 같아도 다르다