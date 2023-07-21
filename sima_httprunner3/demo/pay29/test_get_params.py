from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase


class TestGetGoods(HttpRunner):
    config = (
        Config("分页查询商品")
        .base_url("http://124.70.221.221:8201")
        .verify(verify=False)
    )
    teststeps = [
        Step(
            RunRequest("分页查询商品-步骤1")
            .get("/api/v1/goods")
            .with_params(**{"page":1,"size":2})
            .validate()
            .assert_equal("status_code",200)
            .assert_equal("body.code",0)
            .assert_equal("body.msg","success!")
        )
    ]