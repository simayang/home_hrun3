from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase

class TestUrlcoded(HttpRunner):
    config = (
        Config("键值对格式请求")
        .base_url("http://124.70.221.221:8201")
        .variables(**{"user":"test","psw":"123456"})
    )
    teststeps = [
        Step(
            RunRequest("键值对格式-登录请求")
            .post("/api/v4/login")
            .with_data({"username":"$user","password":"$psw"})
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.code",0)
            .assert_equal("body.msg","login success!")
            .assert_equal('headers.\"Content-Type\"',"application/json")
        )
    ]