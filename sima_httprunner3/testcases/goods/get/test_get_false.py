from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase
import sys
from pathlib import Path

sys.path.insert(0,str(Path(__file__).parent.parent.parent.parent))

from testcases.login_yml.login_test import TestCaseLogin as login

class TestGetFalse(HttpRunner):

    config = (Config("查询-失败用例")
              .base_url("${ENV(base_url)}")
              .variables(**{"sp_id":"100000"}))

    teststeps = [
        Step(RunTestCase("添加商品").call(login).export(*["token"])),
        Step(RunRequest("查询一个不存在的商品")
             .get("/api/v1/goods/$sp_id")
             .validate()
             .assert_equal("body.code",1000)
             .assert_equal("body.msg","no info")
             )
    ]

if __name__ == '__main__':
    TestGetFalse()