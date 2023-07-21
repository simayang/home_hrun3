from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase,Parameters
import pytest

class Testwuxiao(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "user-psw-email":[
                    ["", "123456", "123@qq.com"],
                    ["a", "123213xx", "123456@qq.com"],
                    ["aaaaaaaaaaabbbbbbbbbcccccccccc123", "", "123@qq.com"],
                    ["testx123", "", "123@qq.com"],
                    ["testx123", "12345", "123@qq.com"],
                    ["testx123", "123456789123456789", "123@qq.com"],
                    ["testx123", "1234546", "12345"]
                ]
            }
        ),
    )

    def test_start(self,param):
        super().test_start(param)

    config = (
        Config("注册-反向场景用例-用例")
        .base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(
            RunRequest("注册-反向-步骤")
            .post("/api/v1/register")
            .with_json({"username":"$user","password":"$psw","email":"$email"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 3003)
        )
    ]