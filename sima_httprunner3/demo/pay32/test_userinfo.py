from  httprunner import HttpRunner, Config,Step,RunRequest,RunTestCase

from demo.test_login import TestLoginCase

class TestUserInfo(HttpRunner):
    config = (Config("引用登录用例，取token给当前接口用")
        .base_url("http://124.70.221.221:8201")
    )

    teststeps = [
        Step(
            RunTestCase("步骤1——引用登录")
            .call(TestLoginCase)
            .export(*["token"])
        ),

        Step(
            RunRequest("取到token后放在请求头")
            .get("/api/v1/userinfo")
            .with_headers(**{"Authorization":"Token $token"})
            .validate()
            .assert_equal("body.code",0)
        )
    ]

