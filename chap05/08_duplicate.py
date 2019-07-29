
# 중첩 함수

import math as m

def stddev(*args):
    def mean(): # 중첩함수
        return sum(args)/ len(args)

    def variance(m): # 중첩함수
        total = 0
        for arg in args:
            total += (arg - m) ** 2
        return  total/ (len(args)-1)
    v = variance(mean())
    return  m.sqrt(v)

print(stddev(2.3,1.7,1.4,0.7,1.9)) # 0.6

# print(mean()) # 중첩함수는 외부에서 호출 불가능.

# pass : 기능이 구현을 잠시 미루자
def empty_function():
    pass            # void method(){}와 같은 역할.



