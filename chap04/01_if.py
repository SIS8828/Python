# 자료형
# - bool 자료형 : True/ false
a = 5 > 3
# 비교연산자 : >, <, >=, <=, ==, !=

print(type(a)) # <class 'bool'>


# 논리 연산자 : and, or, not
print(not True) #False

b = ( 5 > 3 ) and (7 < 5) #False

print(b)

# 조건문 (if)
print('수를 입력하세요')
num = eval(input())

import sys

if num == 0:
    print("0은 나눗셈에 이용할 수 없습니다.")
    sys.exit(0)
else:
    print("3/",num,'=',3/num)

############################
