# 변수명 규칙
# - 문자, 숫자, (_) 가능. 단, 숫자로 시작할 수 없음
# - 대/소문자 구별.
# - 예약어 사용 불가능

#########################
## 수치형: int,Long,float, complex ##
#########################

a = 123456789
print(a)# 123456789
print(type(a)) #<class 'int'>

## 연산자(+,-,*,/,//,%)

a = 3 +4
print(a)

b = 7 - 10
print(b)

c = 7 * -3
print(c)

d = 30 // 7
print(d)

e = 22 / 7
print(e)

f = 22 // 7
print(f)

g = 22 % 7
print(g)

# 진수변환
# 16진수 -> 10진수
print(0x3039) #12345

# 10진수 -> 16진수
print(hex(12345)) #0x3039

print(type(hex(12345))) #<class 'str'>

# 10진수 -> 2진수
print(bin(0))
print(bin(8))
print(bin(16))
print(bin(255))
'''
0b0
0b1000
0b10000
0b11111111
'''
print(type(bin(255))) # <class 'str'> 자료형이 문자열

# 2진수 -> 10 진수
print(0b0) # 0
print(0b11111111) # 255

# 10 진수 -> 8진수 변환
print(oct(8)) # 0o10
print(oct(12)) # 0o14
print(oct(254)) # 0o376

# 변수 (실수)
h = 3.14
print(h)
print(type(h))

# 연산자
b = 3.3 + 4.2
print(b)

c = 10.0 + 30.8
print(c)

d = 10.1 * 30.4
print(d)

e = 22.5 /7.6
print(e)
print(type(e)) #<class 'float'>

f = 22.5 // 7.6 # 결과값 : 실수 , 몫 반환연산자
print(f)           # 2.0

g = 22.5 % 7.6 # 결과값 : 실수, 나머지 반환연산자
print(g) # 7.300000000000001

# 복소수(complex Number)
a = 2 + 3j
print(a)
print(type(a)) #<class 'complex'>
print(a.real) # 2.0
print(a.imag) # 3.0
print(a.conjugate()) # 켤레복소수

# 복소수의 사칙연산
a = (1+2j)+(3+4j)
print(a) #(4+6j)

a = (1+2j)*(3+4j)
print(a) #(-5+10j)

a = (1+2j)/(3+4j)
print(a) #(0.44+0.08j)

# math 모듈을 이용한 계산
import math

print(math.pi) # 원주율
print(math.e) # 자연상수

print(abs(10)) # 절대값 계싼 함수(내장함수)
print(abs(-10))

print(round(1.2)) # 반올림
print(round(1.5))

print(math.trunc(1.4)) # 버림함수

print(math.pow(3,3)) # 3**3 과 동일
print(3**3) # 3^3 = 27
print(math.sqrt(81)) # 제곱근연산

print(math.log(4,2))























