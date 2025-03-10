import pytest

from cpp_stats.metrics.metric_calculator import Metric
from cpp_stats.metrics.number_of_classes import NumberOfClassesCalculator, NumberOfClassesMetric

import utils.clang
import clang.cindex

def test_when_add_two_noc_metrics_then_sum_values():
    m1 = NumberOfClassesMetric(1)
    m2 = NumberOfClassesMetric(2)
    expected = 3

    _, actual = (m1 + m2).get()

    assert expected == actual

def test_when_sum_with_unknown_metric_then_not_implemented():
    m1 = NumberOfClassesMetric(1)
    m2 = Metric("some metric")

    with pytest.raises(NotImplementedError):
        m1 + m2

@pytest.mark.skipif(
    (utils.clang.clang_index() is None),
    reason="Clang cannot be found using env variable LIBCLANG_LIBRARY_PATH"
)
def test_when_definition_then_assert_class(clang_index: clang.cindex.Index):
    calculator = NumberOfClassesCalculator()
    tu = clang_index.parse(".\\tests\\data\\analyze\\definition.hpp", args=['-x', 'c++'])
    c1_class = None
    for child in tu.cursor.get_children():
        if child.kind == clang.cindex.CursorKind.CLASS_DECL and child.displayname == "C1":
            c1_class = child
            break
    if c1_class is None:
        assert False
    expected = 1

    metric = calculator(c1_class)

    _, actual = metric.get()
    assert expected == actual

@pytest.mark.skipif(
    (utils.clang.clang_index() is None),
    reason="Clang cannot be found using env variable LIBCLANG_LIBRARY_PATH"
)
def test_when_declaration_then_assert_not_class(clang_index: clang.cindex.Index):
    calculator = NumberOfClassesCalculator()
    tu = clang_index.parse(".\\tests\\data\\analyze\\declaration.hpp", args=['-x', 'c++'])
    c1_class = None
    for child in tu.cursor.get_children():
        if child.kind == clang.cindex.CursorKind.CLASS_DECL and child.displayname == "C1":
            c1_class = child
            break
    if c1_class is None:
        assert False
    expected = 0

    metric = calculator(c1_class)

    _, actual = metric.get()
    assert expected == actual
