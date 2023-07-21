import hashlib

"""
第1步: 将所有参数（注意是所有参数），除去sign本身，以及值是空的参数，按参数名字母升序排序。
第2步: 然后把排序后的参数按参数1值1参数2值2…参数n值n（这里的参数和值必须是传输参数的原始值，不能是经过处理的，如不能将"转成”后再拼接）的方式拼接成一个字符串。
第3步: 把分配给接入方的验证密钥key拼接在第2步得到的字符串key。
第2步: 在上一步得到的字符串后面加上验证密钥key(这里的密钥key是接口提供方分配给接口接入方的)，然后计算md5值，得到32位字符串，然后转成大写.
第4步: 计算第3步字符串转小写后得到的md5值(32位)，得到的字符串作为sign的值。

假设传输的数据是http://www.xxx.com/interface.aspx?sign=sign_value&p2=v2&p1=v1&method=cancel&p3=&pn=vn
（实际情况最好是通过post方式发送），
其中sign参数对应的sign_value就是签名的值。
第一步，接字拼符串，首先去除sign参数本身，然后去除值是空的参数p3，剩下p2=v2&p1=v1&method=cancel&pn=vn，
然后按参数名字符升序排序，method=cancel&p1=v1&p2=v2&pn=vn.
第二步，然后做参数名和值的拼接，最后得到methodcancelp1v1p2v2pnvn
第三步，在上面拼接得到的字符串后加上验证密钥key，我们假设是abc，得到新的字符串methodcancelp1v1p2v2pnvnabc
第四步，然后将这个字符串换为小写进行md5计算，假设得到的是abcdef，这个值即为sign签名值。
注意，计算md5之前请确保接口与接入方的字符串编码一致，如统一使用utf-8编码或者GBK编码，如果编码方式不一致则计算出来的签名会校验失败
"""

apikey = "12345678" # 验证密钥，由公司开发提供

body = {
    "username":"test",
    "password":"123456",
    "mail":""
}

for i in body.items():
    # print(i)
    if i[0] != "sgin" and i[1] !="":
        print("i[0]:",i[0])
        print("i[1]:",i[1])

# b  = [j for j in body.items()]
# print(b)

# a  = ["".join(j) for j in body.items()]
# print(a)


# 第一步+第二步：

# 首先拿出非sign本身及空的参数，把它们拼接在一起
a = ["".join(i) for i in body.items() if i[0] and i[1] != "sign" and i[1] !=""]
print(a)


# 参数名ASCII码从小到大排序,ASCII码，只需要知道排序时默认就是按照ASCII码排的即可
strA = "".join(sorted(a))
print(strA)

# 第三步，在上面拼接得到的字符串后加上验证密钥key，我们假设是abc，得到新的字符串methodcancelp1v1p2v2pnvnabc
striSignTemp = strA+apikey
print(striSignTemp)
print(type(striSignTemp))

# 第四步，将得到的内容转换为小写，进行md5加密

# 固定的md5加密写法
def jiamimd5(src):
    m = hashlib.md5()
    m.update(str.encode('UTF-8'))
    return m.hexdigest()

# lower是字符串内置函数，把字符串内容转换为小写
sign = jiamimd5(striSignTemp.lower())
print(sign)

# 得到sign签名后新的body值
body["sign"] = sign
print(body)