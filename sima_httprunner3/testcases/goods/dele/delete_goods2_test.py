# NOTE: Generated By HttpRunner v3.1.5
# FROM: testcases\goods\dele\delete_goods2.yml


import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent))


import pytest
from httprunner import Parameters


from httprunner import HttpRunner, Config, Step, RunRequest, RunTestCase

from testcases.login_yml.login_test import TestCaseLogin as Login

from testcases.goods.add.add_good_status_null_test import (
    TestCaseAddGoodStatusNull as AddGoodStatusNull,
)


class TestCaseDeleteGoods2(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "goodsname-goodscode-merchantid-merchantname-goodsprice-stock-goodsgroupid-price-goodsstatus": [
                    [
                        "sima_add",
                        "${goods_code()}",
                        "10003",
                        "《东方甄选》",
                        "50",
                        "100",
                        "1",
                        "30",
                        "1",
                    ]
                ]
            }
        ),
    )
    def test_start(self, param):
        super().test_start(param)

    config = Config("登录、添加商品、删除商品").base_url("${ENV(base_url)}")

    teststeps = [
        Step(RunTestCase("登录").call(Login).export(*["token"])),
        Step(RunTestCase("添加商品").call(AddGoodStatusNull).export(*["dele_spid2"])),
        Step(
            RunRequest("删除商品")
            .delete("/api/v1/goods/$dele_spid2")
            .validate()
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", "success!")
        ),
    ]


if __name__ == "__main__":
    TestCaseDeleteGoods2().test_start()
