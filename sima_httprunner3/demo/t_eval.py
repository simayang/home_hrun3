# eval()是python中功能非常强大的一个函数
# 将字符串当成有效的表达式来求值，并返回计算结果
# 所谓表达式就是：eval这个函数会把里面的字符串参数的引号去掉，
# 把中间的内容当成Python的代码，eval函数会执行这段代码并且返回执行结果


# 计算1+1
restult = eval("1+1")
print(restult)

# 打印5个+
restult1 = eval("'+' * 5")
print(restult1)


# 将字符串转换成列表
restult2 = eval("[1,2,3,4]")
print(restult2)

# 将字符串转换成字典
restult3 = eval("{'name':'小甲鱼'}")
print(restult3)


# 用一个超简单的案例来运用一下eval函数 —— 计算器
# 要求：
# 1. 提示用户输入一个加减乘除混合运算
# 2. 返回计算结果

input_number = input("请输入一个加减乘除运算公式：")  # 例如输入：1+2*3/4
print(eval(input_number))

