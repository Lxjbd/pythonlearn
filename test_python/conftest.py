import pytest
import yaml
import os

from test_python.pythoncode.cal_test import Calculator

yaml_path = os.path.dirname(__file__) + "/cal_data.yml"

with open(yaml_path) as  f:
    datas = yaml.safe_load(f)
    add_datas = datas["add"]
    sub_datas = datas["sub"]
    mul_datas = datas["mul"]
    div_datas = datas["div"]


@pytest.fixture(scope="module", params=add_datas)
def get_add(request):
    print("\n开始计算")
    data = request.param
    yield data
    print("\n计算结束")


@pytest.fixture(scope="module", params=sub_datas)
def get_sub(request):
    print("\n开始计算")
    data = request.param
    yield data
    print("\n计算结束")


@pytest.fixture(scope="module", params=mul_datas)
def get_mul(request):
    print("\n开始计算")
    data = request.param
    yield data
    print("\n计算结束")


@pytest.fixture(scope="module", params=div_datas)
def get_div(request):
    print("\n开始计算")
    data = request.param
    yield data
    print("\n计算结束")


@pytest.fixture(scope="module")
def get_calc():
    print("获取计算器实例")
    calc = Calculator()
    return calc
