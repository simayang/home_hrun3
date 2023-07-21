import pytest

# 参数化

class Testdemo(object):

    # 引用mark.parametrize 装饰器，进行参数化

    # 参数是都在一个字符串里面的，包括参数化的参数和期望结果
    @pytest.mark.parametrize("test_input,expected",
                             [
                                 ("5+3",8),
                                 ("6*9",54)
                             ])

    def test_a(self,test_input,expected):
        assert eval(test_input) == expected