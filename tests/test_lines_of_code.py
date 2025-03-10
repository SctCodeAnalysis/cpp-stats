'''
Tests module lines_of_code.py
'''
from pathlib import Path

import pytest

from cpp_stats.metrics.metric_calculator import Metric
from cpp_stats.metrics.lines_of_code import LinesOfCodeCalculator, LinesOfCodeMetric

def test_regular_1():
    '''
    Tests that in file `./tests/data/repo/main.cpp` LOC calculator finds 6 lines.
    '''
    files = [
        Path('./tests/data/repo/main.cpp')
    ]
    calculator = LinesOfCodeCalculator()
    expected = 6

    _, actual = calculator(files).get()

    assert expected == actual , f"Expected: {expected}, Actual: {actual}"

def test_regular_2():
    '''
    Tests that in file `./tests/data/repo_with_ignr_modules/src/serial_port.c`
    LOC calculator finds 1 line.
    '''
    files = [
        Path('./tests/data/repo_with_ignr_modules/src/serial_port.c')
    ]
    calculator = LinesOfCodeCalculator()
    expected = 1

    _, actual = calculator(files).get()

    assert expected == actual , f"Expected LOC value: {expected}, Actual: {actual}"

def test_metric_add_operation_1():
    '''
    Tests add operation of two LOC metrics.
    '''
    first = LinesOfCodeMetric(5)
    second = LinesOfCodeMetric(1)
    expected = 6

    _, actual = (first + second).get()

    assert expected == actual, f"Expected LOC value: {expected}, Actual: {actual}"

def test_metric_add_operation_2():
    '''
    Tests add operation of two LOC metrics.
    '''
    first = LinesOfCodeMetric(0)
    second = LinesOfCodeMetric(0)
    expected = 0

    _, actual = (first + second).get()

    assert expected == actual, f"Expected LOC value: {expected}, Actual: {actual}"

def test_not_implemented_add_operation_1():
    '''
    Tests exception during add operation of LOC and non LOC metrics.
    '''
    first = LinesOfCodeMetric(12)
    second = Metric("some metric")

    with pytest.raises(NotImplementedError):
        _, _ = first + second

def test_not_implemented_add_operation_2():
    '''
    Tests exception during add operation of LOC metrics and other class.
    '''
    first = LinesOfCodeMetric(12)
    second = 2

    with pytest.raises(NotImplementedError):
        _, _ = first + second
