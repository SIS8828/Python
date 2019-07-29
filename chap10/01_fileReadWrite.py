# file에 write 하기

file = open('test.txt','w')
file.write('hello')
file.close()

# file에 read 하기

file = open('test.txt','r')
# file = open('test.txt')
# file = open('test.txt','t')
# file = open('test.txt', 'rt')



str = file.read()
print(str)
file.close()

'''

'''