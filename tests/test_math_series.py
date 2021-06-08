from math_series import __version__
from math_series.series import *


def test_version():
    assert __version__ == '0.1.0'

# fibonacci Testing  0, 1, 1, 2, 3, 5, 8, 13, ...


def test_fibonacci_zero():
    expected = 0
    actual = fibonacci(0)
    assert actual == expected


def test_fibonacci_one():
    expected = 1
    actual = fibonacci(1)
    assert actual == expected


def test_fibonacci_seven():
    expected = 13
    actual = fibonacci(7)
    assert actual == expected

# Lucas Number Testing:: 2, 1, 3, 4, 7, 11, 18, 29, ...


def test_lucas_zero():
    expected = 2
    actual = lucas(0)
    assert actual == expected


def test_lucas_one():
    expected = 1
    actual = lucas(1)
    assert actual == expected


def test_lucas_eleven():
    expected = 11
    actual = lucas(5)
    assert actual == expected


def test_sum_series_first():
    expected = 5
    actual = sum_series(5, 0, 1)
    assert actual == expected


def test_sum_series_second():
    expected = 29
    actual = sum_series(7, 2, 1)
    assert actual == expected


def test_sum_series_2():
    expected = 27
    actual = sum_series(4, 3, 7)
    assert expected == actual
