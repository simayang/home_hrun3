from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase,Parameters
import sys
import pytest
from pathlib import Path
from testcases.login_yml.login_test import TestCaseLogin as Login

# 将路径添加到临时变量，程序退出时结束
sys.path.insert(0,str(Path(__file__).parent.parent.parent))

# print(Path(__file__).parent.parent.parent)
class TestDeleteGoods(HttpRunner):
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

    def test_start(self,param):
        super().test_start(param)

    config = (Config("删除商品")
              .base_url("${ENV(base_url)}")
              .export(*["dele_spid"])
              )
    teststeps = [
        Step(RunTestCase("登录").call(Login).export(*["token"])),
        Step(
            RunRequest("添加商品")
            .post("/api/v1/goods")
            .with_headers(**{"Authorization": "Token $token"})
            .with_json(
                {
                    "goodsname": "$goodsname",
                    "goodscode": "$goodscode",
                    "merchantid": "$merchantid",
                    "merchantname": "$merchantname",
                    "goodsprice": "$goodsprice",
                    "stock": "$stock",
                    "goodsgroupid": "$goodsgroupid",
                    "price": "$price",
                    "goodsstatus": "$goodsstatus",
                }
            )
            .extract()
            .with_jmespath("body.data.id", "dele_spid")
            .validate()
            .assert_equal("status_code", 200)
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", "success!")
        ),
        Step(
            RunRequest("删除商品")
            .delete("/api/v1/goods/$dele_spid")
            .validate()
            .assert_equal("body.code", 0)
            .assert_equal("body.msg", "success!")
        ),
    ]

if __name__ == '__main__':
    TestDeleteGoods().test_start()