import sys
from pathlib import Path

import os

# os方法获取当前文件的位置 :D:\test\hrun\sima_httprunner3\testcases\goods\put\test-path.py
print(os.path.abspath(__file__))

# pathlib 方法获取当前文件的位置:D:\test\hrun\sima_httprunner3\testcases\goods\put\test-path.py
print(Path(__file__))
print(Path(__file__).resolve())
print("当前文件所在目录，类似pwd:"+str(Path.cwd()))
print("当前文件家目录，："+str(Path.home()))

# OS方法 获取当前文件所在是文件夹:D:\test\hrun\sima_httprunner3\testcases\goods\put
print(os.path.dirname(os.path.abspath(__file__)))

# pathlib 方法获取当前文件所在文件夹:D:\test\hrun\sima_httprunner3\testcases\goods\put
print("Path获取当前文件夹"+ str(Path(__file__).resolve().parent))

# OS方法，获取上级目录 :D:\test\hrun\sima_httprunner3\testcases\goods
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 使用 pathilb方法获取上级目录:D:\test\hrun\sima_httprunner3\testcases\goods
print(Path(__file__).resolve().parent.parent)


print(Path(__file__).parent.parent.parent)


# 自己尝试获取testcases下面的login_yml

# a = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # 先找到外层testcases目录
# print(a)
# b = os.path.join(a,'login_yml','login.yml') # 然后join拼接外层目录下面的文件路径
# print(b)
#
# f = open(b,'r',encoding='utf-8') # open以r可读的方式打开b位置的文件
# ff = f.read() # 读取打开的文件
# print(ff)


