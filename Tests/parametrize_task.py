from distutils.command.config import config
import os
import sys
import pytest
import yaml


def get_numbers_data(config_name):
    module_dir = os.path.dirname(os.path.abspath(sys.modules[__name__].__file__))
    parent_dir = os.path.dirname(module_dir)
    with open(os.path.join(parent_dir, 'Configs', config_name), 'r') as stream:
        config = yaml.safe_load(stream)
    return config['cases']


def add_numbers(a, b, c):
    try:
        return a + b + c
    except TypeError:
        raise 'Please check the parameters. All of them must be numeric'


@pytest.mark.smoke
@pytest.mark.parametrize(
    "input_data, expected",
    [(data["input"], data["expected"]) for data in get_numbers_data("config.yaml")],
    ids=[data["case_name"] for data in get_numbers_data("config.yaml")]
)
def test_add_numbers(input_data, expected):
    result = add_numbers(*input_data)
    assert result == expected, f"Expected {expected} but got {result}"


@pytest.mark.critical
@pytest.mark.parametrize(
    "num1, num2, num3",
    [("2", 3, 5), (1, 5, None), ([], 2, 3)],
    ids=["StringType", "NoneType", "ListType"]
)
def test_add_floats(num1, num2, num3):
    a, b, c = 'a', 2, 1
    with pytest.raises(TypeError):
        add_numbers(a, b, c)
