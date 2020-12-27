import allure
import pytest


@allure.feature("计算器模块")
class TestCalc:

    @pytest.mark.run(order=1)
    @allure.story("加法")
    def test_add1(self, get_calc, get_add):
        result = get_calc.add(get_add[0], get_add[1])
        assert result == get_add[2]

    @pytest.mark.run(order=4)
    @allure.story("除法")
    def test_div1(self, get_calc, get_div):
        result = get_calc.div(get_div[0], get_div[1])
        assert result == get_div[2]

    @pytest.mark.run(order=2)
    @allure.story("减法")
    def test_sub1(self, get_calc, get_sub):
        result = get_calc.sub(get_sub[0], get_sub[1])
        assert result == get_sub[2]

    @pytest.mark.run(order=3)
    @allure.story("乘法")
    def test_mul1(self, get_calc, get_mul):
        result = get_calc.mul(get_mul[0], get_mul[1])
        assert result == get_mul[2]
