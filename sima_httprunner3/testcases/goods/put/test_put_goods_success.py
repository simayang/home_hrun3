import sys
from pathlib import Path
from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase
from testcases.login_yml.login_test import TestCaseLogin

# 将路径添加到临时变量，程序退出时结束
sys.path.insert(0,str(Path(__file__).parent.parent.parent.parent))

class TestPutGoods(HttpRunner):
    config = (Config("修改用例-自写")
              .base_url("${ENV(base_url)}")
              .variables(**{
                    "id": 77783,
                    "goodsname": "sima_add",
                    "goodscode": "sp_1687965910",
                    "merchantid": 10003,
                    "merchantname": "《东方甄选_大SB》",
                    "goodsprice": 30,
                    "stock": 100,
                    "goodsgroupid": 3,
                    "price": 30,
                    "goodsstatus": 1,
                    }
                )
            )

    teststeps = [
        Step(RunTestCase("取登录的token").call(TestCaseLogin).export(*["token"])),
        Step(RunRequest("修改商品")
             .put("/api/v1/goods/$id") # v1其实并不依赖登录，这样写是看一下引用其他用例的格式
             .with_json(
                    {
                    "id": "$id",
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
                .validate()
                .assert_equal("body.code",0)
             )
    ]