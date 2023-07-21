from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase, Parameters
import pytest


class TestZhuce(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters({"user-psw-email": "${get_user2()}"}),
    )
    def test_start(self,param):
        super().test_start(param)

    config = (
        Config("注册成功")
        .base_url("http://124.70.221.221:8201")
    )

    teststeps = [
        # Step(
        #     RunTestCase("引用debugtalk")
        #     .call(user_register())
        # ),

        Step(
            RunRequest("注册-成功，步骤")
            .post("/api/v1/register")
            .with_json({"username": "$user", "password": "$psw", "email": "$email"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
        )
    ]
