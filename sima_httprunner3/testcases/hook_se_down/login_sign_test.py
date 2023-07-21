# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\hook_se_down\login_sign.yml


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseLoginSign(HttpRunner):

    config = (
        Config("sign签名")
        .variables(**{"user": "test1", "psw": "123456"})
        .base_url("${ENV(base_url)}")
    )

    teststeps = [
        Step(
            RunRequest("登录-签名")
            .setup_hook("${setup_request($request)}")
            .post("/api/v3/login")
            .with_json({"username": "$user", "password": "$psw"})
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", "login success!")
            .assert_length_equal("body.token", 40)
        ),
    ]


if __name__ == "__main__":
    TestCaseLoginSign().test_start()