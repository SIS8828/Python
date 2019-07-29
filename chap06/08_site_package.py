import sys

print(sys.path)

#['C:\\workspaces\\python\\chap06',
# 'C:\\workspaces\\python\\chap06',
# 'C:\\workspaces\\python\\chap04',
# 'C:\\workspaces\\python\\chap05',
# 'C:\\ProgramData\\Anaconda3\\envs\\tf_cpu\\python36.zip',
# 'C:\\ProgramData\\Anaconda3\\envs\\tf_cpu\\DLLs',
# 'C:\\ProgramData\\Anaconda3\\envs\\tf_cpu\\lib',
# 'C:\\ProgramData\\Anaconda3\\envs\\tf_cpu',
# 'C:\\ProgramData\\Anaconda3\\envs\\tf_cpu\\lib\\site-packages']

from my_package2 import  my_module

if __name__ == "__main__":
    my_module.info()
