from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase

class TestLoginCase(HttpRunner):
    config= (
        Config("登录用例")
        .base_url("http://124.70.221.221:8201")
        .variables(**{"user":"test","psw":"123456"})
        .export(*["token"])

    )


    teststeps= [
        Step(
            RunRequest("登录")
            .post("/api/v1/login")
            .with_json({"username":"${user}","password":"${psw}"})
            .extract()
            .with_jmespath("body.token","token")
            .validate()
            .assert_equal("body.code",0,message="code错误")
            .assert_equal("body.msg","login success!",message="登录失败")
    )
    ]

