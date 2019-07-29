# 한 함수안에 여러개의 ruturn 배치 가능

def my_arg1(arg):
    if arg < 0 :
        return arg * -1
    else:
        return  arg

# 주의 필요

def my_arg2(arg):
    if arg < 0:
        return arg * -1
    else:
        return
result = my_arg2(-1)
print(result)

result = my_arg2(0)
print(result) # return을 실행하지 못하고 함수가 종료되면
                # 함수는 호출자에게 None을 반환

def ogamdo (num):
    for i in range(1, num+1):
        print('제 {0}의 아해'.format(i))
        if i == 5 :
            return #2. 데이터 없이 함수종료의 의미로 사용

ogamdo(3)
print()
ogamdo(5)
print()
ogamdo(8)
print()


def print_someting(*args):
    for s in args:
        print(s)

print_someting(1,2,3,4,5)

# 3. 반환 경과 없고, 함수 중간에
# 종료 시킬 일도 없을 때
# return문 생략 가능