from httprunner import HttpRunner,Config,Step,RunTestCase,RunRequest
import pytest

class TestChongFuZhuce(HttpRunner):
    config = (
        Config("重复注册用例")
        .base_url("http://124.70.221.221:8201")
        .variables(**{"user":"test","psw":"123456"})
              )

    teststeps = [
        Step(
            RunRequest("重复注册用例-步骤")
            .post("/api/v1/register")
            .with_json({"username":"$user","password":"$psw"})
            .validate()
            .assert_equal("body.code",2000)
            .assert_equal("body.msg","test用户已被注册")
        )
    ]