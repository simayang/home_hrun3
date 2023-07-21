from pathlib import Path

print("当前文件的绝对路径："+str(Path(__file__)))
print("当前文件的绝对路径，另一种写法："+str(Path(__file__).resolve()))

# 获取testcases下的login_py文件夹下的test_login.py
a = Path(__file__).parent.parent.parent
print(a /'login_py/test_login.py')

# 获取当前目录项目跟目录
print(Path(__file__).parent.parent.parent.parent)

print("当前文件所在文件夹："+str(Path(__file__).parent))
print("当前文件所在文件夹的父目录："+str(Path(__file__).parent.parent))

print("当前文件所在目录的test-path.py文件："+str(Path(__file__).parent/ 'test-path.py'))

"""
示例1
"""
print(Path.cwd()) # 你当前py文件的所在目录，类似于pwd
print(Path.home()) # 你当前用户的家目录（windows比如C:\Users\用户名）


"""
示例2
"""
a = Path(__file__)
print("对象类型是：",type(a)) # <class 'pathlib.WindowsPath'>
print("当前文件的绝对路径：",a)

b = Path("test_path2.py")
print("当前文件的相对路径：",b)
print("当前文件的绝对路径另一种写法：",b.resolve())

parent_dir = Path(__file__).parent #还可以继续.parent，相当于cd ..和cd ../..
print('当前文件的父目录:',parent_dir)
print('路径拼接用/(忽略操作系统差异): ',parent_dir / a) #


"""
获取路径组成部分
"""
saolei_apk = Path(r'D:\test\hrun\sima_httprunner3\testcases\goods\put\test_path2.py')
print(saolei_apk)
print(saolei_apk.name) # name 文件名，包含后缀名，如果是目录则获取目录名
print(saolei_apk.stem) # 文件名，不包含后缀。如果没有后缀名返回空
print(saolei_apk.suffix) # 只获取后缀名
print(saolei_apk.parent) # 当前文件的父级目录，相当于用命令进入后的 cd..
print(saolei_apk.anchor) # 目录前面的部分，也就是在哪个盘下 （目录前面的部分 C:\）

# 多级目录
for parent in saolei_apk.parents: # 依次往上输出，直到最跟目录 D:\
    print(parent) #


# 如果是os模块，要获取其父目录用的是os.path.dirname()，多级目录的话就比较麻烦，下面可以对比一下
# PS：用r标记路径 只不过是定义了 变量把要操作的目录标记了出来，即以标记的目录进行操作

import os
import arrow

print("os获取当前文件的绝对路径："+str(os.path.abspath(__file__)))
os_saolei_apk = os.path.dirname(r"D:\test\hrun\sima_httprunner3\testcases\goods\put\test_path2.py")
print(os_saolei_apk)
print("当前文件所在目录的上级目录:"+ os.path.dirname(os_saolei_apk))
print("当前文件所在目录的上上级目录（每多获取一个上级层级多输入一次os.path.dirname）:"+
      os.path.dirname(os.path.dirname(os_saolei_apk)))




# 如果是用 pathlib的话：
pathlib_saolei_apk = Path(__file__) # 当前目录所在路径
print("当前文件的上一级目录：",pathlib_saolei_apk.parent)
print("当前文件的上上一级目录：",pathlib_saolei_apk.parent.parent) # 就相当于cd..多次
print(pathlib_saolei_apk.parents[0]) # 你还可以用parents，注意0是第一层所在目录，1是父目录，2是爷目录....
print(pathlib_saolei_apk.parents[1]) # 你还可以用parents，注意0是第一层所在目录，1是父目录，2是爷目录....



"""
获取文件属性
"""

pathlib_saolei_apk1 = Path(__file__)
print(pathlib_saolei_apk1.stat())

mtime = pathlib_saolei_apk1.stat().st_atime
print(arrow.get(mtime).format("YYYY-MM-DD HH:MM:SS")) # arrow第三方库是操作时间的


"""
文件（夹）操作
"""

# 示例

# newfile = Path(r"D:\test\hrun\sima_httprunner3\testcases\goods\put\20230701.txt")
#
# if not newfile.exists():
#     print("创建文件")
#     newfile.touch(exist_ok=True)
#     newfile.open(mode='r',encoding='utf-8')
#     newfile.write_text("123456")
#
# else:
#     pass
#     print("删除文件")
#     newfile.unlink()



"""
批量移动
"""

def move_file_to(srcdir,dstdir,file_pattern):
    file = Path(srcdir).rglob(file_pattern)
    for _ in file:
        Path(_).replace(Path(dstdir)/ Path(_).name) # 第一个位置下的txt格式的，移动到第二个形参dstdir路径下，path.name # 文件名


move_file_to(srcdir=r'D:\test\hrun\sima_httprunner3\testcases\goods\put\20230701.txt',
             dstdir=r'D:\test\hrun\sima_httprunner3\testcases\goods',
             file_pattern='*.txt')


"""
批量修改后缀
"""


def change_suffix(dst_dir,old_suffix,new_suffix):
    file = Path(dst_dir).rglob('*.'+old_suffix)
    if list(file):
        for _ in file:
            new_ = Path(_).with_suffix('.'+new_suffix)
            Path(_).replace(new_)
    else:
        raise Exception('file-type:{} not found(recursive) in {}'.format(old_suffix,dst_dir))
change_suffix(dst_dir=r'e:\test',old_suffix='txt',new_suffix='docx')
change_suffix(dst_dir=r"D:\test\hrun\sima_httprunner3\testcases\goods\20230701.txt",
              old_suffix='txt',
              new_suffix='yml')



"""
统计目录下的文件类型
"""

import collections

# 不能递归的，只能在当前目录下找
path_1 = Path(r"D:\test\hrun\sima_httprunner3\testcases\goods")
files = [f.suffix for  f in path_1.iterdir() if f.is_file()]
print(dict(collections.Counter(files)))


# 能递归的，找当前目录下所有文件夹和文件的类型
path = Path(r'D:\test\hrun\sima_httprunner3\testcases\goods')
files = [f.suffix for f in path.rglob('*.*') if f.is_file()]
print(dict(collections.Counter(files)))
