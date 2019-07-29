print('수를 입력하세요')
num = eval(input())
print(type(num))


if num == 0:
    print("0은 나눗셈에 이용할 수 없습니다.")
else:
    print("프로그램 수행")
    print("3/",num,'=',3/num)

