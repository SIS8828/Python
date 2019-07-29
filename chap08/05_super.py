# super() : 부모 클래스의 객체 역할을 하는 프록시(Proxy)
#               를 반환하는 내장 함수

class A:
    def __init__(self):
        print("A.__init__ 호출")
        self.message = "Hello"

class B(A):
    def __init__(self):
        print("B.__init__() 호출.")

        super().__init__()
        print("self.message is " + self.message)

if __name__ == '__main__':
    b = B()

    print(b.message)

########################################
## 참조 : 자식 클래스의 인스턴스를 생성할 떄 부모 클래스의
##          __init__()를 메서드가 자동 호출.
########################################


class Base:
    def __init__(self):
        print("Base")

class Derived(Base):
    pass

    # def __init__(self):
    #    super().__init__()

d = Derived()


