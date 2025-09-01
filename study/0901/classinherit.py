class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("동물이 소리를 냅니다.")

    def info(self):
        print(f"이름: {self.name}, 나이: {self.age}살")

class Dog(Animal):
    def make_sound(self):
        print("멍! 멍!")

class Cat(Animal):
    def make_sound(self):
        print("야옹! 야옹!")

    def purr(self):
        print("고양이가 기분 좋게 그르렁거립니다.")

# Animal 클래스 객체 생성
animal = Animal("익명", 5)
animal.info()
animal.make_sound()
print("-" * 20)

# Dog 클래스 객체 생성
my_dog = Dog("뽀삐", 3)
my_dog.info()        # 부모 클래스(Animal)의 info 메서드 사용
my_dog.make_sound()  # 오버라이딩된 make_sound 메서드 사용
print("-" * 20)

# Cat 클래스 객체 생성
my_cat = Cat("냥냥이", 2)
my_cat.info()        # 부모 클래스(Animal)의 info 메서드 사용
my_cat.make_sound()  # 오버라이딩된 make_sound 메서드 사용
my_cat.purr()        # Cat 클래스만의 고유 메서드 사용