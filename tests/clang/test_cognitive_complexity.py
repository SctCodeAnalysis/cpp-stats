import pytest

from cpp_stats.metrics.metric_calculator import Metric
from cpp_stats.metrics.cognitive_complexity import MeanCognitiveComplexityCalculator, MaxCognitiveComplexityCalculator
from cpp_stats.metrics.cognitive_complexity import MeanCognitiveComplexityMetric, MaxCognitiveComplexityMetric, _calculate_cognitive_complexity

import clang.cindex

def test_merge_mean_metric_data():
    m1 = MeanCognitiveComplexityMetric(1, 1)
    m2 = MeanCognitiveComplexityMetric(10, 1)
    expected_value = 11
    expected_cnt = 2

    m3 = m1 + m2
    actual_value = m3.sum_value
    actual_cnt = m3.cnt

    assert expected_value == actual_value
    assert expected_cnt == actual_cnt

def test_merge_max_metric_data():
    m1 = MaxCognitiveComplexityMetric(10)
    m2 = MaxCognitiveComplexityMetric(100)
    expected = 100

    actual = (m1 + m2).value

    assert expected == actual

def test_when_sum_with_unknown_metric_then_not_implemented_1():
    m1 = MeanCognitiveComplexityMetric(10, 1)
    m2 = Metric("some metric")

    with pytest.raises(NotImplementedError):
        m1 + m2

def test_when_sum_with_unknown_metric_then_not_implemented_2():
    m1 = MaxCognitiveComplexityMetric(100)
    m2 = Metric("some metric")

    with pytest.raises(NotImplementedError):
        m1 + m2

def test_calculate_complexity_sum_of_primes(clang_index: clang.cindex.Index):
    tu = clang_index.parse("./tests/data/analyze/cognitive_complexity.hpp", args=['-x', 'c++'])
    func = None
    for child in tu.cursor.walk_preorder():
        if (child.kind == clang.cindex.CursorKind.FUNCTION_DECL
            and child.displayname == "sumOfPrimes(int)"):
            func = child
            break
    if func is None:
        assert False
    expected = 7

    actual = _calculate_cognitive_complexity(func)

    assert expected == actual

def test_calculate_complexity_for_myFunc(clang_index: clang.cindex.Index):
    tu = clang_index.parse("./tests/data/analyze/cognitive_complexity.hpp", args=['-x', 'c++'])
    func = None
    for child in tu.cursor.walk_preorder():
        if (child.kind == clang.cindex.CursorKind.FUNCTION_DECL
            and child.displayname == "myFunc()"):
            func = child
            break
    if func is None:
        assert False
    expected = 2

    actual = _calculate_cognitive_complexity(func)

    assert expected == actual

def test_happy_path_get_mean_metric():
    m = MeanCognitiveComplexityMetric(10, 2)
    expected = 5

    _, actual = m.get()

    assert expected == actual

def test_empty_path_get_mean_metric():
    m = MeanCognitiveComplexityMetric(0, 0)
    expected = 0

    _, actual = m.get()

    assert expected == actual

def test_get_mean_max():
    m = MaxCognitiveComplexityMetric(5)
    expected = 5

    _, actual = m.get()

    assert expected == actual

def test_get_valid_metric_for_mean(clang_index: clang.cindex.Index):
    tu = clang_index.parse("./tests/data/analyze/cognitive_complexity.hpp", args=['-x', 'c++'])
    func = None
    calc = MeanCognitiveComplexityCalculator()
    for child in tu.cursor.walk_preorder():
        if child.kind == clang.cindex.CursorKind.FUNCTION_DECL and child.displayname == "sumOfPrimes(int)":
            func = child
            break
    if func is None:
        assert False
    expected_analyzed_funcs = 1

    actual_analyzed_funcs = calc(func).cnt

    assert expected_analyzed_funcs == actual_analyzed_funcs

def test_get_empty_metric_for_mean(clang_index: clang.cindex.Index):
    tu = clang_index.parse("./tests/data/analyze/number_of_methods.hpp", args=['-x', 'c++'])
    func = None
    calc = MeanCognitiveComplexityCalculator()
    for child in tu.cursor.walk_preorder():
        if child.kind == clang.cindex.CursorKind.CLASS_DECL and child.displayname == "C1":
            func = child
            break
    if func is None:
        assert False
    expected_analyzed_funcs = 0

    actual_analyzed_funcs = calc(func).cnt

    assert expected_analyzed_funcs == actual_analyzed_funcs

def test_get_valid_metric_for_meax(clang_index: clang.cindex.Index):
    tu = clang_index.parse("./tests/data/analyze/cognitive_complexity.hpp", args=['-x', 'c++'])
    func = None
    calc = MaxCognitiveComplexityCalculator()
    for child in tu.cursor.walk_preorder():
        if child.kind == clang.cindex.CursorKind.FUNCTION_DECL and child.displayname == "sumOfPrimes(int)":
            func = child
            break
    if func is None:
        assert False

    actual = calc(func).value

    assert actual != 0

def test_get_empty_metric_for_max(clang_index: clang.cindex.Index):
    tu = clang_index.parse("./tests/data/analyze/number_of_methods.hpp", args=['-x', 'c++'])
    func = None
    calc = MaxCognitiveComplexityCalculator()
    for child in tu.cursor.walk_preorder():
        if child.kind == clang.cindex.CursorKind.CLASS_DECL and child.displayname == "C1":
            func = child
            break
    if func is None:
        assert False
    expected = 0

    actual = calc(func).value

    assert actual == expected
