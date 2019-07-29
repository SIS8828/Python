coffee = 10
money = 300

while money :
    print("커피를 준다")
    coffee  -= 1
    print("남은커피양은 %d개 입니다." % coffee)
    if coffee == 0:
        print("매진 판매종료")
        break