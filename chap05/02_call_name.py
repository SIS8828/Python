# 호출과 변환

## 함수 정의하기

def my_abs(arg):
    if(arg < 0):
        result = arg * -1
    else:
        result = arg

    return result

# print(my_abs()) # error - 입력데이터(인자) 넣어주지 않아서

print(my_abs(123))

my_abs(123)
print(my_abs) # 할당된 주소값 반환
print(0x0000000002052EA0)

print(globals())



































