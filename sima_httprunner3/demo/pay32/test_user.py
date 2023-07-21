from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase
from demo.test_login import TestLoginCase

class TestUserInfoCase(HttpRunner):
        config = Config("case").base_url("http://124.70.221.221:8201")
        teststeps = [
            Step(RunTestCase("step1-login")
                 .call(TestLoginCase)
                 .export(*["token"])),
            Step(RunRequest("step2-info")
                 .get("/api/v1/userinfo")
                 .with_headers(**{"Authorization": "Token $token"})
                 .validate()
                 .assert_equal("body.code", 0))
        ]
