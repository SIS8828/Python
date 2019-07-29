print('요일(월~일)을 입력하세요 \n')
dow = input()
print(type(dow))
if dow == '월':
    print('Monday')
elif dow == '화':
    print('Tuesday')
elif dow == '수':
    print('wednesday')
elif dow == '목':
    print('Thursday')
elif dow == '금':
    print('Friday')
elif dow == '토':
    print('Saturday')
elif dow == '일':
    print('Sundat')
else:
    print("잘못입력하였습니다.")
