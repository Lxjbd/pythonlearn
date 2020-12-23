import pytest
import yaml

from pythoncode.cal_test import Calculator


def setup_module():
    print("\n即将开始执行测试用例")


def teardown_module():
    print("\n测试用例执行完毕")


def read_files():
    with open("./cal_data.yml") as f:
        datas = yaml.safe_load(f)
        add_datas = datas["add"]
        sub_datas = datas["sub"]
        mul_datas = datas["mul"]
        div_datas = datas["div"]
        return [add_datas, sub_datas, mul_datas, div_datas]


class TestCal:
    def setup_class(self):
        self.calc = Calculator()
        print("\n类开始前执行")

    def teardown_class(self):
        print("\n类结束后执行")

    def setup(self):
        print("\n开始计算")

    def teardown(self):
        print("\n计算结束")

    @pytest.mark.parametrize("a,b,expect", read_files()[0])
    def test_add(self, a, b, expect):
        result = self.calc.add(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", read_files()[1])
    def test_sub(self, a, b, expect):
        result = self.calc.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", read_files()[2])
    def test_mul(self, a, b, expect):
        result = self.calc.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize("a,b,expect", read_files()[3])
    def test_div(self, a, b, expect):
        result = self.calc.div(a, b)
        assert result == expect