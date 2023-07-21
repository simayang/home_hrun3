import requests

s = requests.Session()
r1 = s.request(method="GET",url="http://124.70.221.221:8201/api/test/demo")
print(r1.text)

body = {
    "username":"test",
    "password":"123456"
}
r2 = s.request(method="POST",json=body,url="http://124.70.221.221:8201/api/v1/login")
print(r2.text)


r3 = s.request(method="GET",url="http://124.70.221.221:8201/api/v1/goods",params={
    "page": 1,
    "size": 2
})
print(r3.text)

r4 = s.request(method="POST",url="http://124.70.221.221:8201/api/v4/login",data={
    "username":"test1",
    "password": "123456"
})
print(r4.text)