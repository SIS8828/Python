# 문자열

a = 'hello, python'
print (a)

b = "hello, python"
print(b)

c = '''
봄날의 속잎나고, 얼마나 못할 창공에 곧 불어 피고 위하여 철환하였는가? 인생에 이것은 때
까지 크고 너의 뭇 구하기 부패뿐이다. 보이는 커다란 사는가 보라. 관현악이며, 오직 같으며, 
사람은 천하를 듣는다. 인간에 청춘의 없으면 이상은 소리다.이것은 많이 그리하였는가? 그들
의 품으며, 위하여 꽃이 약동하다. 얼음과 천하를 만물은 밝은 내려온 새 말이다. 곳이 같은 역
사를 곳으로 피는 노래하며 커다란 위하여서. 속잎나고, 크고 인간에 목숨을 꽃 교향악이다.'''
print(c)

d= """
봄날의 속잎나고, 얼마나 못할 창공에 곧 불어 피고 위하여 철환하였는가? 인생에 이것은 때
까지 크고 너의 뭇 구하기 부패뿐이다. 보이는 커다란 사는가 보라. 관현악이며, 오직 같으며, 
사람은 천하를 듣는다. 인간에 청춘의 없으면 이상은 소리다.이것은 많이 그리하였는가? 그들
의 품으며, 위하여 꽃이 약동하다. 얼음과 천하를 만물은 밝은 내려온 새 말이다. 곳이 같은 역
사를 곳으로 피는 노래하며 커다란 위하여서. 속잎나고, 크고 인간에 목숨을 꽃 교향악이다.
"""

print(d)
print(type(d)) #<class 'str'>

#문자열 연산(+, *)
print("hello","python")
print("hello"+"python")
print("hello"* 2 + "python")

hello = "hello, "
world = "world!!!"
helloworld = hello + world
print(helloworld)

# 주의
age = 25
# print("방가방가"+age)  자료형이 같이야 출력가능
print("방가방가 "*5) #문자열 반속

s = 'Good Morning'
print(s[0:4])

a = s[:4] # = s[0:4]
b = s[5:] # = s[5:12]
c = s[-3:]
print(a)
print(b)
print(c)

d = s[::2] # 두칸씩 카운팅
print(d)

print('M' in s) # true
print('Good' in s)

print(len(s )) # 12

# str 객체 제공 메서드
## - pdf 참조

hello = "how do you do, how do you do"
print(hello.count('do'))




# 텍스트 -> 수
'''
print("첫번째 수 입력 : ")
num1 = int(input())
print("두번째 수 입력 : ")
num2 = int(input())

result = num1 * num2

print("{0} * {1} = {2}".format(num1,num2,result))
'''
# 수 -> 텍스트
import math

print(type(math.pi)) #<class 'float'>

text = "원주율은"  + str(math.pi) + "입니다."
print(text)

str = 'hello python!'

print(str.startswith('hell'))

print(str.find('el'))
print(str.find('python'))

str2 = 'am'
str3 = 'I am a boy,  I am a student'

print(str2 in str3)
print('you' in str3)

print(str.upper())
print(str.lower())
print(str.swapcase())
print(str.capitalize())
print(str.title())













