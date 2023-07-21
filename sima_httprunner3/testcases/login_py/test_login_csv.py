import pytest
from httprunner import HttpRunner,Step,Config,RunRequest,RunTestCase
from httprunner import Parameters


class TestLoginCsv(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {"user-password":"${parameterize(data/user_password2.yml)}"}
        )
    )
    def test_start(self,param):
        super().test_start(param)

    config = (
        Config("登录-参数化")
        .base_url("http://124.70.221.221:8201")
    )

    teststeps = [
        Step(
            RunRequest("登录参数化-步骤")
            .post("/api/v1/login")
            .with_json({"username":"$user","password":"$password"})
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.code",0)
        )
    ]

