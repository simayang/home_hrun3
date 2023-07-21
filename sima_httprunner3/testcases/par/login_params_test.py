# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\par\login_params.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginParams(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "user": ["test1", "test2", "test3", "test4"],
                "psw": ["123456", "123456", "123456", "123456"],
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("login case").base_url("${ENV(base_url)}")

    teststeps = [
        Step(
            RunRequest("step login")
            .with_variables(**{"password": 123456})
            .post("/api/v1/login")
            .with_json({"username": "$user", "password": "$password"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", "login success!")
            .assert_length_equal("body.token", 40)
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginParams().test_start()
