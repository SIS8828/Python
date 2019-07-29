# 데코레이터 사용 용도(생성자)

class MyDecorator:
    def __init__(self,f):

        print("Initializing My Decorator")
        self.func = f

    def __call__(self):
        print("Begin : {0}".format(self.func.__name__))

        self.func()

        print("End:{0}".format(self.func.__name__))


if __name__ == '__main__':
    @MyDecorator
    def print_hello():
        print("Hello")
    print_hello()

