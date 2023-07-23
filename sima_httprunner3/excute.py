import pytest
import os

# pytest执行脚本并生成测试结果文件到report/allure_raw目录下
# encoding: utf-8
pytest.main(['-s','--alluredir','allure_report'])

# 将report/allure_raw目录下的结果文件生成html类型的测试报告到report/allure_raw目录下
# -o report/html --clean 是清空已有的测试报告再生成
os.system(r'allure generate allure_report -o allure_report/html --clgitean')