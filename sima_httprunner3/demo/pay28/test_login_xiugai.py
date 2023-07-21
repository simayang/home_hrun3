from httprunner import  HttpRunner,Config,Step, RunRequest, RunTestCase

class TestCaseLogin(HttpRunner):
    config = (
        Config("用例描述-登录用例")
        .base_url("http://124.70.221.221:8201")
        .verify(verify=False)
        .variables(**{"user":"test","psw":"123456"})
        .export(*["token"])
    )

    teststeps = [
        Step(
            RunRequest("登录")
            .post("/api/v1/login")
            .with_json({"username": "$user", "password": "$psw"})
            .extract()
            .with_jmespath("body.token","token")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.msg","login success!")
        ),
        Step(
            RunRequest("修改个人信息")
            .post("/api/v1/userinfo")
            .with_headers(**{"Authorization":"Token $token"})
            .with_json(
                {
                    "name": "$user",
                    "sex": "M",
                    "age": 21,
                    "mail": "283340479@qq.com"
                }
            )
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.code",0)
            .assert_equal("body.message","update some data!")
        )
    ]