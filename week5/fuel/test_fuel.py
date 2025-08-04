import pytest

from fuel import convert, gauge


def test_convert_error():
    
    with pytest.raises(ValueError):
        convert("12/1")
        convert("hello/10")
    
    with pytest.raises(ZeroDivisionError):
        convert("12/0")


def test_gauge():
    assert gauge(12) == "12%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"