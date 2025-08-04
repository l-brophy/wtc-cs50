import pytest

from twttr import shorten


def test_normal():
    assert shorten("hello world") == "hll wrld"


def test_case():
    assert shorten("Hello, World!") == "Hll, World!"


def test_num():
    assert shorten("h3llo w0rld") == "h3ll w0rld"