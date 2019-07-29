# 변수의 유효범위 (scope_

def scope_test1():
    a = 1
    print('a:{0}'.format(a))

a = 0

scope_test1()
print('a:{0}'.format(a))

def scope_test2():
    global c # global 키워드:전역변수, 지역변수의
    c = 1   # 함수 호출시 메모리 생성
    print('c:{0}'.format(c))


c = 0
print(c)
scope_test2()
print('c:{0}'.format(c))





