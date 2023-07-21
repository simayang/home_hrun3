body = {
    "code": 0,
    "msg": "成功success!",
    "data": [
        {
            "age": 20,
            "create_time": "2019-09-15",
            "id": 1,
            "mail": "283340479@qq.com",
            "name": "yoyo",
            "sex": "M"
        },
        {
            "age": 21,
            "create_time": "2019-09-16",
            "id": 2,
            "mail": "123445@qq.com",
            "name": "yoyo111",
            "sex": "M"
        }
    ]
}

import jmespath

# 1.提取code值

res1 = jmespath.search('code',body)
print(res1)

# 2.msg值
res2 = jmespath.search('msg',body)
print(res2)

# 3.提取data数据

res3 = jmespath.search('data',body)
print(res3)

# 4.提取data数据中第一条数据

res4 = jmespath.search('data[0]',body)
print(res4)

# 5.提取data数据中name# 的值为yoyo的邮箱

res5 = jmespath.search('data[*].name',body)
print(res5)

res6 = jmespath.search("data[?name == 'yoyo']",body)
print(res6)

res6_1 = jmespath.search("data[].name",body)
print(res6_1)


res7 = jmespath.search("data[?name == 'yoyo'].mail|[0]",body)
print(res7)

# 6.提取data数据组中，年龄大于20的个数

res8 = jmespath.search("length(data[?age>`20`])",body)
print(res8)
