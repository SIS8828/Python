print('수를 입력하세요')
num = int(input())

if num > 10 and num % 2 == 0:
        print('10보다 큰 짝수')
elif num > 10 and num % 2 != 0:
        print('10보다 큰 홀수')
elif num < 10 and num % 2 == 0:
        print('10보다 작은 짝수')
elif num < 10 and num % 2 != 0:
        print('10보다 작은 홀수')
else:
    print('입력값을 확인하세요.')
