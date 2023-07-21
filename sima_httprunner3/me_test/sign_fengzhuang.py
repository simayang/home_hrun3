import hashlib

"""
假设传输的数据是http://www.xxx.com/interface.aspx?sign=sign_value&p2=v2&p1=v1&method=cancel&p3=&pn=vn
（实际情况最好是通过post方式发送），
其中sign参数对应的sign_value就是签名的值。
第一步，拼接字符串，首先去除sign参数本身，然后去除值是空的参数p3，剩下p2=v2&p1=v1&method=cancel&pn=vn，
然后按参数名字符升序排序，method=cancel&p1=v1&p2=v2&pn=vn.
第二步，然后做参数名和值的拼接，最后得到methodcancelp1v1p2v2pnvn
第三步，在上面拼接得到的字符串后加上验证密钥key，我们假设是abc，得到新的字符串methodcancelp1v1p2v2pnvnabc
第四步，然后将这个字符串换为小写进行md5计算，假设得到的是abcdef，这个值即为sign签名值。
注意，计算md5之前请确保接口与接入方的字符串编码一致，如统一使用utf-8编码或者GBK编码，如果编码方式不一致则计算出来的签名会校验失败。
"""

def sign_body(body,apikey="12345678"):
    # 第一步：去除sign本身和值为空的参数，拼接起来，并升序排序
    a = ["".join(i) for i in body.items() if i[0] and i[1] != "sign" and i[1] !=""]
    print(a)
    strA = "".join(sorted(a))
    print(strA)

    # 第二步：拼接好的内容 加上apikey
    strB = strA+apikey

    # 第三步：进行md5加密
    def jiamimd5(src):
        m = hashlib.md5()
        m.update(src.encode('UTF-8'))
        return m.hexdigest()
    sign = jiamimd5(strB.lower())

    # 最后返回新的body
    body["sign"]= sign

    return body

if __name__ == '__main__':
     body = {
        "username": "test",
        "password": "123456",
        "mail": "",
        "sign": ""
    }
     print(sign_body(body,apikey="12345678"))


