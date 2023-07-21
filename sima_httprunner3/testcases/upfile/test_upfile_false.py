from httprunner import HttpRunner,Config,Step,RunRequest,Parameters
import pytest

class TestUpFileFalse(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "filename-titlename-code-msg":[
                    ["data/test.png", "", 400, "bad request"],
                    ["", "上海-悠悠", 400, "bad request"],
                ]
            }
        ),
    )

    def test_strat(self,param):
        super().test_start(param)

    config = Config("上传失败").base_url("${ENV(base_url)}")
    teststeps = [
        Step(RunRequest("上传失败")
            .post("/api/v1/upfile/")
            .upload(**{"file": "$filename", "title": "$titlename"})
            .validate()
            .assert_equal("body.code", "$code")
            .assert_equal("body.msg", "$msg")
        ),
    ]