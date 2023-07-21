# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\zhuce_yml\test_zhuce.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseTestZhuce(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "user-psw-email": [
                    ["${user_register()}", "123456", ""],
                    ["${user_register()}", "123456", "61961262@qq.com"],
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("注册-成功").base_url("${ENV(base_url)}")

    teststeps = [
        Step(
            RunRequest("注册-成功")
            .post("/api/v1/register")
            .with_json({"username": "$user", "password": "$psw", "email": "$email"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        ),
    ]


if __name__ == "__main__":
    TestCaseTestZhuce().test_start()