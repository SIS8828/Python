# Iterator와 순회 가능한 객체

iterator = range(3).__iter__()
print(iterator.__next__())
print(iterator.__next__())
print(iterator.__next__())
# print(iterator.__next__()) # error


##############################################

class MyRange:  # range() 함수와 같은 일을 하는 클래스 정의
    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.end:
            current = self.current
            self.current += 1
            return current
        else:
            raise StopIteration()

if __name__ == '__main__':

    for i in range(5):
        print(i)

    print("============================")


    for i in MyRange(0,5):
        print(i)

    print("============================")

    iterator = MyRange(0,5).__iter__()
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())