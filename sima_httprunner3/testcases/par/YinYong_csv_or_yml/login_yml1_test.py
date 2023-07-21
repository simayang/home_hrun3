# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\par\YinYong_csv_or_yml\login_yml1.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginYml1(HttpRunner):
    @pytest.mark.parametrize(
        "param", Parameters({"username": "${P(data/user_password3.yml)}"})
    )
    def test_start(self, param):
        super().test_start(param)

    config = (
        Config("login case").variables(**{"psw": "123456"}).base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(
            RunRequest("step login")
            .post("/api/v1/login")
            .with_json({"username": "$username", "password": "$psw"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", "login success!")
            .assert_length_equal("body.token", 40)
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginYml1().test_start()
