import pytest

from plates import is_valid


def test_len():
    assert is_valid("h") == False
    assert is_valid("he") == True
    assert is_valid("helloworld") == False


def test_alnum():
    assert is_valid("hello.") == False
    assert is_valid("World!") == False


def test_pos0():
    assert is_valid("0hello") == False
    assert is_valid("0world") == False


def test_consecutive_nums():
    assert is_valid("h3llo") == False
    assert is_valid("hell0o") == False
    assert is_valid("hell0") == False
    assert is_valid("hel10") == True


def test_correct():
    assert is_valid("CS50") == True
    assert is_valid("hlwrld") == True