# 다중상속시 주의 사항

class A:
    def method(self):
        print("A")

class B:
    def method(self):
        print("B")

class C(A):
    def method(self):
        print("C")

class D(B,C):
    pass

if __name__ == '__main__':
    obj = D()
    obj.method()
                    # B -> D(B,C)
                    # C -> D(C,B)


print(D.mro())
