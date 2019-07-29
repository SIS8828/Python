"""
예외처리 구문
try:
    # 문제가 없을 경우 실행 할 코드
except:
     # 문제가 생겼을 때 실행 할 코드

"""

# 예시
'''
try:
    print(10 / 0)
except:
    print("예외가 발생했습니다.")

print("프로그램 종료")
'''

'''
예외처리 구문 2
try:
 # 문제가 없을 경우 실행 할 코드

except 예외형식1:
 # 문제가 생겼을 때 실행 할 코드

except 예외형식2:
 # 문제가 생겼을 때 실행 할 코
'''

# 예시
'''
my_list = [1,2,3]

try:
    print("첨자를 입력하세요 :")
    index = int(input())
    print("나눌 숫자를 입력하세요: ")
    y = int(input())
    print(my_list[index] / y)
except IndexError as i:
    print(i)
except ZeroDivisionError as z:
    print(z)
'''

'''

예외처리 구문 2
try:
 # 문제가 없을 경우 실행 할 코드

except 예외형식1 as i:
 # 문제가 생겼을 때 실행 할 코드

except 예외형식2 as u:
 # 문제가 생겼을 때 실행 할 코
'''

'''
예외처리 구문 4
– try절을 무사히 실행하면 만날 수 있는 else
try:
 # 실행할 코드 블록
except:
 # 예외 처리 코드 블록
else:
 # except절을 만나지 않았을 경우 실행하는 코드 블록
'''
'''
my_list = [1,2,3]

try:
    print("첨자를 입력하세요 :")
    index = int(input())
    print("my_list[{0}]:{1}".format(index,my_list[index]))
except IndexError as i:
    print(i)
else:
    print("출력 성공~")
'''
'''
예외처리 구문
– 반드시 실행되는 finally
try:
 # 코드 블록
except:
 # 코드 블록
else:
 # 코드 블록

finally:
 # 코드 블록
'''

'''
my_list = [1,2,3]

try:
    print("첨자를 입력하세요 :")
    index = int(input())
    print("my_list[{0}]:{1}".format(index,my_list[index]))
except IndexError as i:
    print(i)
else:
    print("출력 성공~")
finally:
    print("무조건~")
'''

''' 
# Exception 클래스

    BaseException
            SystemExit
            Keyboardinterrupt
            GeneratorExit
            Exception
                ....
                ArithmeticError
                    ZeroDivisonError
                    ...
                    
                LookupError
                    IndexError
                    ...


'''
'''
 # 주의
 # 예외문 처리시 상위예외처리문을 먼저 작성하게되면 하위예외처리문이 작동하지 않는다.
my_list = [1,2,3]

try:
    print("첨자를 입력하세요 :")
    index = int(input())
    print(my_list[index] / 0)
except Exception as e :
    print("예외가 발생했습니다.".format(e))
except IndexError as i:
    print("잘못된 인덱스 입니다. {0}".format(i))
except ZeroDivisionError as Zde:
    print("0으로 나눌수 없습니다. {0}".format(Zde))

'''
'''
# 의도적 예외 발생
# ex1)
text = input()
if text.isdigit() == False:
    raise  Exception("입력 받은 문자열이 숫자열로 구성되어 있지 않습니다.")

# ex2) 무조건 예외 발생
# raise Exception("예외를 발생시킵니다.")
'''

'''
# ex3)
try:
    raise  Exception("예외를 발생시킵니다.")
except Exception as err:
    print("예외발생 {0}".format(err))



# ex4)

def some_function():
    print("1~10 사시의 수를 입력하세요: ")
    num = int(input())
    if num < 1 or num > 10 :
        raise Exception("유효하지않은 숫자입니다.{0}".format(num))
    else:
        print("입력한수는 {0}".format(num))

try:
    some_function()
except Exception as err:
    print("예외발생!{0}".format(err))


def some_function():
    print("1~10 사시의 수를 입력하세요: ")
    num = int(input())
    if num < 1 or num > 10 :
        raise Exception("유효하지않은 숫자입니다.{0}".format(num))
    else:
        print("입력한수는 {0}".format(num))
def some_function_caller():
    try:
        some_function()
    except Exception as err:
        print("예외 발생 {0}".format(err))
        raise

try:
    some_function_caller()
except Exception as err:
    print("raise에 의해서 전달된 예외 처리 구문 {0}".format(err))


class MyException(Exception):
    def __init__(self):
        super().__init__("MyException이 발생했습니다.")

if everything_is_fine == False:
    raise  MyException()
'''

class InvalidIntException:
    def __init__(self, arg):
        super().__init__('정수가 아닙니다.: {0}'.format(arg))

def convert_to_integer(text):
        if text.isdigit():  # 부호 (+, -)
            return int(text)
        else:
            raise  InvalidIntException(text)

if __name__ == "__main__":
    try:
        print('숫자를 입력하세요')
        text = input()
        number = convert_to_integer(text)
    except InvalidIntException as err:
        print("에러~ {0}".format(err))
    else:
        print('정수로 변환 : {0}({1})'.format(number,type(number)))
















