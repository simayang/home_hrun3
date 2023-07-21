"""
python中单星号和双星号的区别

这两种用法其实都是用来将任意个数的参数导入到Python函数中

单星号 *agrs 是以元祖的形式导入
双兴号 **kwargs 是以字典的形式导入

"""
# 单星号
def foo(param1,*param2):
    print(param1)
    print(param2)

foo(1,2,3,4,5)


# 双星号
def bar(param1,**param2):
    print(param1)
    print(param2)

bar(1,a=2,b=3)

# 单信号解压参数列表

def foo2(runoob_1,runoob_2):
    print(runoob_1,runoob_2)

l = [1,2]
foo2(*l) # 解压的时候 ，列表参数必须和入参参数数量相同


# 两个用户出现在同一个函数中
def foo3(a,b=10,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

foo3(1,2,3,4,e=5,g=6)
