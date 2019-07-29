
def gennerator():
     yield 0
     yield 1
     yield 2
     yield 3

if __name__ == "__main__":
    iterator = gennerator()
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())
    print(iterator.__next__())

##########################

# class MyRange 동일 기능 정의

def MyRange(start,end):
        current = start

        while current < end :
                yield  current
                current += 1
        return

for i in MyRange(1,10):
    print(i)