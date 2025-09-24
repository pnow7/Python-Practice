# Python에서는 메서드(함수)를 클래스 내부에 정의하고, 매개변수(name, age)를 직접 받아서 처리합니다. 
# Java와 달리 **void**나 자료형(String, int)을 명시적으로 선언할 필요가 없음
class User:
    # 이 메서드는 'self'를 첫 번째 인자로 받음
    # self는 인스턴스 자체를 가리킴
    # 이는 해당 메서드가 클래스의 일부임을 나타냄
    def display_info(self, name, age):
        print(f"Name: {name}")
        print(f"Age: {age}")

# 위 메서드를 호출하는 예시
if __name__ == "__main__":
    # User 클래스의 인스턴스를 생성
    user_instance = User()
    
    # 메서드 호출 시, self를 제외한 인자들을 전달
    user_instance.display_info("Alice", 25)