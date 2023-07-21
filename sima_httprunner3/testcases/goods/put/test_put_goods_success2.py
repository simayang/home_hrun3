from httprunner import HttpRunner,Config,Step,RunRequest,RunTestCase,Parameters
import pytest

class TestPutGoods(HttpRunner):
    @pytest.mark.parametrize(
        "param",
        Parameters(
            {
                "id-goodsname-goodscode-merchantid-merchantname-goodsprice-stock-goodsgroupid-price-goodsstatus":[
                    ["77783","sima_add","sp_1687965910","10003","《东方甄选_大SB》","30","100",3,30,1],
                    ["77783","sima_add","sp_1687965910","10003","《东方甄选_大SB》","30","100",3,30,0],
                    ["77783","sima_add","sp_1687965910","10003","纸上得来终觉浅","30","100",3,30,0],
                    ["77783","sima_add","sp_1687965910","10003"," ","30","100",3,30,0]
                ]
            }
        ),
    )
    def test_start(self,param):
        super().test_start(param)

    config = Config("修改商品-成功的案例").base_url("${ENV(base_url)}")
    teststeps = [
        Step(
            RunRequest("修改商品")
            .put("/api/v1/goods/$id")
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
                    "goodsstatus": "$goodsstatus"
                }
            )
            .validate()
            .assert_equal("body.code",0)
        )
    ]
