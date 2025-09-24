def student_info(name, age, grade, **kwargs):
    """
    학생 정보를 출력하는 함수
    """
    print(f"이름: {name}")
    print(f"나이: {age}")
    print(f"학년: {grade}")
    print(f"추가 정보: {kwargs}")
    print("-" * 20)

# 전달할 데이터 준비
data_list = ['홍길동', 17, 1]
data_dict = {'major': '컴퓨터', 'school': '새싹고등학교'}

# 리스트는 위치 인자로 언패킹, 딕셔너리는 키워드 인자로 언패킹
student_info(*data_list, **data_dict)

# print(**data_dict)가 오류가 나는 이유는 
# ** 연산자가 함수 호출 시에만 유효한 문법이기 때문

# *는 **"키"**를 펼쳐주고, **는 **"키=값"**을 펼쳐줌