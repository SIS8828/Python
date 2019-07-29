
# 함수를 변수에 담아 사용

def print_something(a):
    print(a)

p = print_something

p(123)
p('abc')


# 순서열 / 딕셔너리에도 변수로 담아보기
def plus(a,b) :
    return  a  + b

def minus(a,b):
    return a - b

first = [plus,minus]
print(first[0](1,2)) # plus(1,2) 와 동일
print(first[1](1,2)) # minus(1,2) 와 동일

# 함수의 매개변수에 함수 전달 기능.
def hello_korea():
    print("안녕~")

def hello_english():
    print('hello')

def greet(hello):
    hello()

greet(hello_korea)
greet(hello_english)

# 함수 내에서 함수를 반환

def get_greeting(where):
    if where == 'K':
        return hello_korea
    else:
        return hello_english

hello = get_greeting('T')
hello() # hello
hello = get_greeting('K')
hello() # 안녕~

