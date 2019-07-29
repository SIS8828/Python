# 딕셔너리(dictionary) 자료형

dic = {'애플':'www.apple.com',
       '네이버':'www.naver.com',
       '파이썬':'www.python.org'}

# 데이터 접근 방법
print(dic['애플'])

# 데이터 삽입/ 저장
dic2 = {}
print(type(dic2))

dic2['애플'] = 'www.apple.com'
dic2['네이버'] = 'www.naver.com'
dic2['파이썬'] = 'www.python.org'

print(dic2)

print(dic.keys())
print(dic.values())
print(dic.items())

print('애플' in dic.keys())
print('www.naver.com' in dic.values())

print(dic.pop('애플'))
print(dic)

dic.clear()
print(dic)