# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\upfile\upfile_sucess.yml


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase


class TestCaseUpfileSucess(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {"filename-titlename-code-msg": [["data/test.png", "司马", 0, "success!"]]}
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("上传成功").base_url("${ENV(base_url)}")

    teststeps = [
        Step(
            RunRequest("上传成功")
            .post("/api/v1/upfile/")
            .upload(**{"file": "$filename", "title": "$titlename"})
            .validate()
            .assert_equal("body.code", "$code")
            .assert_equal("body.msg", "$msg")
        ),
    ]


if __name__ == "__main__":
    TestCaseUpfileSucess().test_start()
