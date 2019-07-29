# Tuple 자료형
a = (1,2,3)
print(a)
print(type(a)) #<class 'tuple'>

b = 1,2,3,4
print(type(b)) #<class 'tuple'>

# 주의)

c = (1)
print(c) # 1
print(type(c)) #<class 'int'>

d = (1,)
print(d) # (1,)
print(type(d)) #<class 'tuple'>

# 슬라이싱 기능
x = (1,2,3,4,5,6)
print(x[4:6])

# + 연산자로 튜플간 연산가능
a = [1,2,3]
b = [4,5,6]
print(a+b)

# 개별요소접근방법
print(a[1])

# a[1] = 2 : 데이터 변경 불가능
print(len(a)) # 3

# 튜플 패킹(tuple packing) : 여러가지 데이터를 튜플로 묶는 것
a = 1,2,3
print(a)

# 튜플 언패킹( tuple unpacking) : 각 요소를 여러 개의 변수에 할당하는 것.
data = 'Seoul', 37.541, 126.986

city, latitude, longitude = data
#  data = city, latitude, longitude # error 허용되지 않음.

print(city)
print(latitude)
print(longitude)

# 튜플 제공 메서드
a = ('abc','def','ghi')
print(a.index('ghi'))
# print(a.index('xyz')) # error
























