import pytest

from numb3rs import validate


def test_1():
    assert validate("127.0.0.1") == True


def test_2():
    assert validate("192.168.0.1") == True


def test_3():
    assert validate("192.68.1.1") == True


def test_4():
    assert validate("255.255.255.255") == True


def test_5():
    assert validate("0.0.0.0") == True


def test_6():
    assert validate("1.1.1.1") == True


def test_7():
    assert validate("256.256.256.256") == False