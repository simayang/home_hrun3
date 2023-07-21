
# eval(expression[, globals[, locals]])
# expression ： 表达式。
# globals ： （可选参数)变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
# locals ： (可选参数)变量作用域，局部命名空间，如果被提供，可以是任何映射对象



# #1.eval无参实现字符串转化
s = "1+2+3*5-2"
print(eval(s))

# 2.字符串中有变量也可以
x = 1
print(eval('x+2'))

# 3.字符串转字典
print(eval("{'name':'linux','age':'18'}"))

# 4.eval传递全局变量参数,注意字典里的:age中的age没有带引号，说明它是个变量，而不是字符串。
print(eval("{'name':'linux','age': age}",{"age":1822}))
print(eval("{'name':'linux','age': age}",{"age":1822},{"age":1833}))

# eval传递本地变量，既有global和local时，变量值先从local中查找。
age = 18
print(eval("{'name':'linux','age': age}",{"age":1822},locals()))
print(eval("{'name':'linux','age':age}"))


# eval虽然方便，但是要注意安全性，可以将字符串转成表达式并执行，
# 就可以利用执行系统命令，删除文件等操作。，比如用户恶意输入就会获得当前目录文件

s1 = eval("__import__('os').system('dir')")
