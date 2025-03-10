'''
Tests analyzer.py
'''
from pathlib import Path 

from cpp_stats.analyzer import CodeAnalyzer

def test_loc_metric_1():
    '''
    Tests that Analyzer correctly gets LOC metric.
    '''
    files = [
        Path('./tests/data/repo/main.cpp')
    ]
    analyzer = CodeAnalyzer(files)
    expected = 6

    _, actual = analyzer.metric("LINES_OF_CODE").get()

    assert expected == actual, f"Expected: {expected}, Actual: {actual}"

def test_loc_metric_2():
    '''
    Tests that Analyzer correctly gets LOC metric.
    '''
    files = [
        Path('./tests/data/repo_with_ignr_modules/src/serial_port.c')
    ]
    analyzer = CodeAnalyzer(files)
    expected = 1

    _, actual = analyzer.metric("LINES_OF_CODE").get()

    assert expected == actual, f"Expected: {expected}, Actual: {actual}"

def test_repeated_metric():
    '''
    Tests that Analyzer remembers calculated metric.
    '''
    files = [
        Path('./tests/data/repo/main.cpp')
    ]
    analyzer = CodeAnalyzer(files)
    expected = analyzer.metric("LINES_OF_CODE")

    actual = analyzer.metric("LINES_OF_CODE")

    assert expected == actual, f"Expected: {expected}, Actual: {actual}"


def test_unknown_metric():
    '''
    Tests that Analyzer gives None for unknown metric.
    '''
    files = [
        Path('./tests/data/repo/main.cpp')
    ]
    analyzer = CodeAnalyzer(files)
    expected = None

    actual = analyzer.metric("UNKNOWN_METRIC")

    assert expected == actual, f"Expected: {expected}, Actual: {actual}"
