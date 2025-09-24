# User 클래스 선언
class User:
    # 생성자(Constructor). __init__은 생성자를 나타내는 특별한 메서드입니다.
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 이름과 나이를 출력하는 메서드(반환값이 없는 함수)
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    # 나이를 1년 증가시키고 새로운 나이를 반환하는 메서드(정수형 반환)
    def get_new_age(self):
        self.age += 1
        return self.age

    # 환영 메시지를 반환하는 메서드(문자열 반환)
    def get_greeting(self):
        return f"Hello, {self.name}!"

# 메인 실행 블록
if __name__ == "__main__":
    # User 클래스의 인스턴스(객체) 생성
    user1 = User("Bob", 30)
    user1.display_info()  # 반환값이 없는 메서드 호출

    # 정수형 반환 메서드 호출
    new_age = user1.get_new_age()
    print(f"New Age: {new_age}")

    # 문자열 반환 메서드 호출
    greeting = user1.get_greeting()
    print(greeting)