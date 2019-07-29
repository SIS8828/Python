class Base:

    def __init__(self):
        print(self)
        self.massage = "Hello World"

    def print_massage(self):
        print(self.massage)


class Deroved(Base):
    pass

if __name__ == '__main__':
    base = Base()
    base.print_massage()

    derived = Deroved()
    derived.print_massage()