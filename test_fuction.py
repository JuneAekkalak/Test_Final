from function import validate_weight, process_weight
import pytest


def test_weight_minus():
    input = -1
    expected_result = "Not valid"
    actual_result = validate_weight(input)
    assert expected_result == actual_result


def test_weight_string():
    input = "test"
    expected_result = "input number"
    actual_result = validate_weight(input)
    assert expected_result == actual_result


def test_process_orange_10():
    price = 75
    weight = 10
    expected_result = 750
    actual_result = process_weight(weight, price)
    assert expected_result == actual_result


def test_process_orange_1():
    price = 75
    weight = 1
    expected_result = 75
    actual_result = process_weight(weight, price)
    assert expected_result == actual_result


def test_process_orange_1_2():
    price = 75
    weight = 1.2
    expected_result = 90
    actual_result = process_weight(weight, price)
    assert expected_result == actual_result


def test_process_mango_5():
    price = 80
    weight = 5
    expected_result = 400
    actual_result = process_weight(weight, price)
    assert expected_result == actual_result


def test_process_mango_20():
    price = 80
    weight = 20
    expected_result = 1600
    actual_result = process_weight(weight, price)
    assert expected_result == actual_result


def test_process_mango_2_5():
    price = 80
    weight = 2.5
    expected_result = 200
    actual_result = process_weight(weight, price)
    assert expected_result == actual_result


def test_process_watermelon_50():
    price = 50
    weight = 5
    expected_result = 250
    actual_result = process_weight(weight, price)
    assert expected_result == actual_result


def test_process_watermelon_5_5():
    price = 50
    weight = 5.5
    expected_result = 275
    actual_result = process_weight(weight, price)
    assert expected_result == actual_result


def test_process_watermelon_20():
    price = 50
    weight = 20
    expected_result = 1000
    actual_result = process_weight(weight, price)
    assert expected_result == actual_result


def test_process_watermelon_string():
    price = 50
    weight = "test"
    expected_result = "input number"
    actual_result = process_weight(weight, price)
    assert expected_result == actual_result


def test_process_watermelon_minus():
    price = 50
    weight = -1
    expected_result = "Not valid"
    actual_result = process_weight(weight, price)
    assert expected_result == actual_result
