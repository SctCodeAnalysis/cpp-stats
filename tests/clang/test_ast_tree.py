from pathlib import Path

import pytest
import clang.cindex

from cpp_stats.metrics.number_of_classes import NumberOfClassesCalculator, METRIC_NAME
from cpp_stats.ast.ast_tree import analyze_ast, _analyze_children
import utils.clang

@pytest.mark.skipif(
    (utils.clang.clang_index() is None),
    reason="Clang cannot be found using env variable LIBCLANG_LIBRARY_PATH"
)
def test_when_nested_then_check_nested_class(clang_index: clang.cindex.Index):
    files = [Path('./tests/data/analyze/nested.hpp')]
    calculators = {METRIC_NAME: NumberOfClassesCalculator()}
    expected = 1

    result = analyze_ast(clang_index, files, calculators)

    _, actual = result[METRIC_NAME].get()
    assert expected == actual
