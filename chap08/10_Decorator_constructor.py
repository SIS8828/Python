# 데코레이터 사용 용도(생성자)

class MyDecorator:
    def __init__(self,f): #init 메서드의 매개변수를 통해
                                # 함수를 받아 들이고 데이터 속성세 저장해둠
        print("Initializing My Decorator")
        self.func = f   # MyDecorator의 func 데이터 속성(필드)이
                            # print_hello 를 저장해둠

    def __call__(self):
        print("Begin : {0}".format(self.func.__name__))

        self.func()

        print("End:{0}".format(self.func.__name__))


if __name__ == '__main__':
    def print_hello():
        print("Hello")

    prt_hello = MyDecorator(print_hello)

    prt_hello()