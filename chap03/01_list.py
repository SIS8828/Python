# 리스트 저장 형태
a = ['홍길동','강감찬','이순신']
print(a)
print(type(a))

# 데이터 접근
print(a[0])
print(a[1])
print(a[2])
# print(a[3]) > error
x = [1,2,3,4,5,6,7,8,9,19]
print(x[:5])

# + 연산자를 통한 리스트간의 결합기능
a = [1,2,3,4,5]
b = [6,7,8,9,19]
print(a+b)

# 특정 위치에 있는 데이터를 변경
a[2] = 7
print(a)

# 리스트 자료형 제공 메서드
a = [1,3,5]
a.append(7)
print(a)

b = [9,11,13]
a.extend(b)
print(a)

c = [11, 13, 15]
a.extend(c)
print(a)

a.insert(1,2)
print(a)

a.remove(13) # 유의 : 삭제 값 지정 (index(x))
print(a)

a.pop() #마지막 요소 제거
print(a)

a.pop(1) # index로 제거
print(a)




a = ['abc','def','ghi']
print(type(a))

print(type(print(type(a.index('abc')))))

a = [1, 100, 2, 100, 3 ,100]

print(a.count(100))

a = [7,5,4,3,2,1,9]
a.sort()
print(a)

a.sort(reverse=True)
print(a)

a= [7,5,9,4,2]
a.reverse()
print(a)

s = ['SUN',1,'MON',2]
print(type(s[0]))
print(type(s[1]))














