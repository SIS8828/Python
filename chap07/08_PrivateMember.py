class YourClass:
    pass

class MyClass :
    def __init__(self):
        self.message = 'hi'

    def some_method(self):
        print(self.message)


obj = MyClass()
obj.some_method()

print('####################################')

class HasPrivate:
    def __init__(self):
        self.public = "P"
        self.__private = "Private"

    def print_from_internal(self):
        print(self.public)
        print(self.__private)

obj = HasPrivate()
obj.print_from_internal()
print('####################################')

print(obj.public)
# print(obj.private) # private에는 접근 불가능
