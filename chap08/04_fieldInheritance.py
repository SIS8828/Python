# 데이터 속성

class A:
    def __init__(self):
        print("A.__init__ 호출")
        self.message = "Hello"

class B(A):
    def __init__(self):
        A.__init__(self)
        print("B.__init__() 호출.")

if __name__ == '__main__':
    b = B()

    print(b.message)
    print(b.message)
    print(b.message)


