class ClassVar:
    text_list = [] # 클래스 멤버 (인스턴스가 공유하는 멤버로 사용됨)

    def add(self, text): # 인스턴스 멤버
        self.text_list.append(text)

    def print_list(self): #
        print(self.text_list)


if __name__ == '__main__':
    a = ClassVar()
    a.add('a')
    a.print_list()

    b = ClassVar()
    b.add('b')
    b.print_list()




