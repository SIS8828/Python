# 인자 이름의 올바른 예

def print_string1(text,count):
    for i in range(count):
        print(text)


print_string1('안뇽',10)

def print_string2(text,count):
    for i in range(count):
        print(text)

print_string2('안뇽2',3)

def print_string3(text,count = 1):
    for i in range(count):
        print(text)

print_string3('hi')

# 키워드 인자 (keyword Argument): 호출자가 매개별수의 이름을
#                                                  일일이 지정해 데이터를 입력하는것
def print_personnel(name, position='staff',nationality='kor'):
    print('name = {0}'.format(name))
    print('position = {0}'.format(position))
    print('nationality = {0}'.format(nationality))

print_personnel('ilsu','CEO','US')

# 가변 매개 변수
def merge_string(*text_list):
    print(type(text_list))
    print(text_list)
merge_string('아버지가','방에','들어간다.')

def merge_string2(*text_list):
    result = ''
    for s in text_list:
        result += s
    return  result
print(merge_string2('아버지가 ','방에',' 들어간다.'))


def print_team(**players):
    print(type(players))

    for k in players.keys():
        print('{0} = {1}'.format(k,players[k]))

print_team(류현진='야구',이강인='축구', 서장훈='농구')

def print_args1(argc, *argv):
    for i in range(argc):
        print(argv[i])

print_args1(3,'홍','감','이')

# 주의
# print_args1(argc=3,'홍','감','이')
# error : 가변 매개변수의 '앞' 에 정의되는 일반매개변수는
#            키워드 매개변수를 이용할 수 없음

def print_args2(*argv, argc):
    for i in range(argc):
        print(argv[i])

print_args2('홍2','감2','이2',argc = 3)

