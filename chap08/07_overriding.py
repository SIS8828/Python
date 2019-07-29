# 다중상속시 주의 사항

class A:
    def method(self):
        print("A")

class B(A):
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")


if __name__ == '__main__':
    a = A()
    a.method() #A

    B().method() # B