import pytest

from bank import value


def test_hello():
    assert value("hello") == 0


def test_h():
    assert value("hey") == 20
    assert value("howdy") == 20
    assert value("How are ya") == 20


def test_anything_else():
    assert value("yahoo") == 100
    assert value("good day") == 100
    assert value("top of the morning") == 100
    assert value("what's up") == 100