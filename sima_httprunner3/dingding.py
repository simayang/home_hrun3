import requests
import json

def teardown_class():
        cont = "自动化测试报告，查看结果链接:http://192.168.3.24:8080/jenkins/job/hrun3_api/"     # 这里要包含新增机器人时候“安全设置”里的关键字，这里是“自动化测试”
        dates = {
            "msgtype": "text",
            "text": {
                "content": cont
            }
        }
        url = "https://oapi.dingtalk.com/robot/send?access_token=54b522177d363386865ee3fe7837444c320629bd9697bdef4ae1ce10c386449e" # 输入上面生成的Webhook地址
        headers = {
            'Content-Type': 'application/json'
        }
        requests.post(url=url, data=json.dumps(dates), headers=headers)

if __name__ == '__main__':
    teardown_class()