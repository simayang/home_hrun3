from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase


class TestLogin(HttpRunner):
    config = (Config("登录-成功")
              .base_url("http://124.70.221.221:8201")
              .export(*["token"])
              .variables(**{"user":"test","psw":"123456"})
              )

    teststeps = [
        Step(
            RunRequest("登录成功-测试步骤")
            .post("/api/v1/login")
            .with_json({"username":"$user","password":"$psw"})
            .extract()
            .with_jmespath("body.token","token")
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.code",0)
        )
    ]