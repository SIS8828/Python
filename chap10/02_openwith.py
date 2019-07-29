'''
자원 누수 방지를 돕는 with ~ as
•구문 형식
with open(파일이름) as 파일객체:
#코드블록
#이곳에서 읽거나
#쓰기를 한 후
#그냥 코드를 빠져나가면 됩니다.

'''
'''
lines = "hihihi"


with open('test.txt','r') as file:
    str = file.read()
    print(str)
    # file.close()  호출할필요 없다.
'''

'''

# 컨텍스트 매니저를 제공하는 함수여서 with문과 함께 사용할 수 있음
# 컨텍스트 매니저(Context Manager) : __enter() 메서드와 __exit__() 구현하고 있는 객체
# with문은 컨텍스트 매니저를 획득한후 코드 블록의
# 실행을 시작할 때 컨텍스트 매니저의 __enter__() 메서드를
# 호출하고, 코드블록이 끝날 때 __exit__()메서드를 호출.

# ex) open() 함수의 기본적인 기능 구현해 보기

class open2():
    def __init__(self, path):
        print('init')
        self.file = open(path)

    def __enter__(self):
        print('enter')
        return  self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        self.file.close()
        return True
"""
with open2("test.txt") as file:
    s = file.read()
    print(s)
"""

file = open2("test.txt")
print(file)
'''
####################################

'''
# @contextmanager 데코레이터로 컨텍스트 매니저 구현하기

from contextlib import contextmanager

@contextmanager 데코레이터로 함수 수식
def 함수이름() :
        # 자원 획득
        try:    __enter__() 역할
            yield 자원 # yield문을 통해 자원 반환: with문의 코드블록이 시작
        finally:    __exit__() 역할
            # 자원해제
            
            
        1. try ~ finally 블록을 갖고 있다.
        2. try 블록에서는 yield 문을 통해 자원을 반환.
            이떄 , yield문은 자신의 매개변로 넘겨진 자원을 반환한 뒤
            임시적으로 현재 함수의 실행르 정지.
            yield에 의해 정지된 함수는 with문의 코드 블록이 실행이 끝날 때 다시 실행
        3. finally 블록에서 획득한 자원을 해제.
            
'''
'''

# ex)

from contextlib import contextmanager

@contextmanager
def open3(path):
    print("opening file...")
    file = open(path)

    try:
        print("yelding file")
        yield file
    finally:
        print("closing file")
        file.close()

with open3("test.txt") as file:
    s = file.read()
    print(s)
'''



"""
# 텍스트 파일 읽기 /쓰기

    1. 문자열을 담은 리스트를 파일에 스는 writelines() 메서드
"""

#ex1)
'''
lines =["we'll find a way we always have - Interstellar\n",
        "I'll find you and I'll kill you - Taken\n",
        "I'll be back - Terminator 2\n"]

with open('movie_quotes.txt','w') as file:
    for line in lines:
        file.write(line)
)
'''


# ex2)
'''
lines =["we'll find a way we always have - Interstellar\n",
        "I'll find you and I'll kill you - Taken\n",
        "I'll be back - Terminator 2\n"]

with open('movie_quotes.txt','w') as file:
    file.writelines(lines)
'''

# ex3)

'''
텍스트 파일 읽기
    2. 줄 단위로 텍스트를 읽는 readline()  & readlines() 메서드
    
'''

# ex1)

'''
with open("movie_quotes.txt",'r') as file:
    line = file.readline()

    while line != ' ':
        print(line, end='')
        line = file.readline()

'''

#ex2)

with open("movie_quotes.txt",'r') as file:
    lines = ''
    lines = file.readlines() # 리스트 형으로 반환
    print(lines)
    for line in lines:
        print(lines, end='')
