import time
from pprint import pprint
from urllib import response
from utils.connect_mysql import DbConnet,dbinfo
import hashlib
import requests


from httprunner import __version__


def get_httprunner_version():
    return __version__


def sum_two(m, n):
    return m + n


def sleep(n_secs):
    time.sleep(n_secs)


def get_user():
    return [
        {"user": "test1"},
        {"user": "test2"},
        {"user": "test3"},
        {"user": "test4"}
    ]


def get_user_psw(n):
    accounts = []
    for i in range(1,n+1):
        accounts.append({
            "user":"test%s" %i,
            "psw": "123456"
        })
    # b = pprint(accounts,width=50)
    return accounts

def get_user_psw2():
    return [
        {"user": "test","psw":"123456"},
        {"user": "test1","psw":"123456"},
        {"user": "test2","psw":"123456"},
        {"user": "test3","psw":"123456"}
    ]


def user_register():
    user_zh = "test"+str(+int(time.time()))
    time.sleep(1)
    return user_zh

def get_user2():
    return [
        {"user":user_register(),"psw":"123456","email":""},
        {"user":user_register(),"psw":"123456","email":"123213@qq.com"},
    ]



def goods_code():
    goodscode = "sp_"+str(+int(time.time()))
    time.sleep(0.3)
    return goodscode


def hook_up():
    print("-----------------------setup!------------------")

def hook_down():
    print("-----------------------teardown!------------------")

def request_sign(request):
    """
    请求sign签名
    """

    # request实际上是一个字典，字典里面要获取json，这里用到的是req_json，对应request请求里面的json请求体
    print("请求body:",request.get("req_json"))
    # 新增 sign参数
    request['req_json']['sign'] = "sign xxxxxxx" # 这一步是对request请求里面的 sign赋值 sign xxxx
    print("sgin签名后的 请求body:",request.get("req_json"))

def response_status(response):
    print("捕捉原本的状态码:",response.status_cdoe)

    response.status_cdoe = 203
    print("查看修改后的reseponse status_cdoe:",response.status_cdoe)

def reaponse_status (response) :
    print ("返回response status_code: ", response.status_code)
    response.status_code = 203
    # if __name__ == '__main__':
#     print(response_status(response_status(response=200)))
    print ("修改后response status_code: ", response.status_code)




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
    # a = ["".join(i) for i in body.items() if i[0] and i[1] != "sign" and i[1] !=""]
    a = ["".join(i) for i in body.items() if i[1] and i[0] != "sign"]
    # print(a)
    strA = "".join(sorted(a))
    # print(strA)

    # 第二步：拼接好的内容 加上apikey
    strB = strA+apikey

    # 第三步：进行md5加密
    def jiamimd5(src):
        m = hashlib.md5()
        m.update(src.encode('UTF-8'))
        return m.hexdigest()
    sign = jiamimd5(strB.lower())
    body["sign"]= sign
    return body

# 把sign签名写成请求预处理
def setup_request(request):
    """发送请求前预处理签名"""

    #request.get获取到 请求内容格式为json的数据
    body = request.get("req_json")
    print("签名前的body:",body)
    # 调用sign签名函数，用此请求body进行签名
    sign = sign_body(body,apikey="12345678")
    print("签名后的body值：",sign)
    # request中更新json格式sign的值为上面签名后的值
    request["req_json"] = sign
    print("request:",request)


def get_goods_spid(sp_id,key=""):
        db = DbConnet(dbinfo)
        ## 查询
        sql1 = "SELECT * from apiapp_goods WHERE id=%s" %sp_id
        result = db.select(sql1)
        print("查询结果为：",result)
        if len(result) == 0:
            return ""
        else:
            result = result[0][key]
            return result




if __name__ == '__main__':
    # body = {"username": "test",
    #     "password": "123456"
    # }
    # print(sign_body(body,apikey="12345678"))
    print(goods_code())
    r = get_goods_spid(sp_id=76719,key="goodsprice")
    print(r)

    print(user_register())