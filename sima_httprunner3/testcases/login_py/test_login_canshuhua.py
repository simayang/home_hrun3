from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase
from httprunner import Parameters
import pytest

class TestLoginFalse(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {"user-psw":[
                ["test1","1234567"],
                ["xxxsad","123456"],
                ["",""]
            ]}
        )
    )
    def test_start(self,param):
        super().test_start(param)
    config = (
        Config("登录-信息错误")
        .base_url("http://124.70.221.221:8201")
    )

    teststeps = [
        Step(
            RunRequest("登录失败-步骤")
            .post("/api/v1/login")
            .with_json({"username":"$user","password":"$psw"})
            .validate()
            .assert_equal("body.code",3003)
        )

    ]
