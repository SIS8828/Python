while True:
    print('반복을 계속할까요?[예/아니오] : ')
    answer = input()

    if answer == '예':
        print('반복 中')
    elif answer == '아니오':
        break
    else:
        print("땡!")

print('End')

