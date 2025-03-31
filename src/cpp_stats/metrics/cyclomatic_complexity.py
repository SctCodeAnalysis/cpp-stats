'''
Module for MEAN_CYCLOMATIC_COMPLEXITY and MAX_CYCLOMATIC_COMPLEXITY metrics.
'''

import clang.cindex

from cpp_stats.metrics.metric_calculator import Metric, ClangMetricCalculator
from cpp_stats.metrics.utils import is_definition_of_func_or_method

MEAN_CYCLOMATIC_COMPLEXITY = 'MEAN_CYCLOMATIC_COMPLEXITY'
MAX_CYCLOMATIC_COMPLEXITY = 'MAX_CYCLOMATIC_COMPLEXITY'

def __need_to_increase(node: clang.cindex.Cursor):
    return node.kind in [
        clang.cindex.CursorKind.IF_STMT,
        clang.cindex.CursorKind.WHILE_STMT,
        clang.cindex.CursorKind.FOR_STMT,
        clang.cindex.CursorKind.CASE_STMT,
        clang.cindex.CursorKind.CONDITIONAL_OPERATOR
    ]

def _calculate_cyclomatic_complexity(node: clang.cindex.Cursor) -> int:
    complexity = 1
    for child in node.walk_preorder():
        complexity += __need_to_increase(child)
    return complexity

class MeanCyclomaticComplexityMetric(Metric):
    '''
    Represents MEAN_CYCLOMATIC_COMPLEXITY metric.
    '''

    def __init__(self, sum_value: int, cnt: int):
        '''
        Initializes metric.
        
        Parameters:
        sum_value (int): sum of cyclomatic complexity values. 
        cnt (int): quantity of viewed functions, methods and lambdas.
        '''
        super().__init__(MEAN_CYCLOMATIC_COMPLEXITY)
        self.sum_value = sum_value
        self.cnt = cnt

    def __add__(self, other):
        if not isinstance(other, MeanCyclomaticComplexityMetric):
            raise NotImplementedError
        return MeanCyclomaticComplexityMetric(
            self.sum_value + other.sum_value,
            other.cnt + self.cnt
        )

    def get(self) -> tuple[str, float]:
        '''
        Returns metric value.
        '''
        value = 0
        if self.cnt != 0:
            value = self.sum_value / self.cnt
        return MEAN_CYCLOMATIC_COMPLEXITY, value

class MeanCyclomaticComplexityCalculator(ClangMetricCalculator):
    '''
    Calculates MEAN_CYCLOMATIC_COMPLEXITY.
    '''

    def __call__(self, node: clang.cindex.Cursor) -> Metric:
        if not self.validate_cursor(node):
            return MeanCyclomaticComplexityMetric(0, 0)
        return MeanCyclomaticComplexityMetric(_calculate_cyclomatic_complexity(node), 1)

    def validate_cursor(self, cursor: clang.cindex.Cursor) -> bool:
        '''
        Validates that given cursor can be used for calculation 
        by this calculator in `__call__`.

        Returns:
        bool: can cursor be used for calculation or not.
        '''
        return is_definition_of_func_or_method(cursor)

class MaxCyclomaticComplexityMetric(Metric):
    '''
    Represents MAX_CYCLOMATIC_COMPLEXITY metric.
    '''

    def __init__(self, value: int):
        '''
        Initializes metric.
        
        Parameters:
        value (int): cyclomatic complexity value.
        '''
        super().__init__(MAX_CYCLOMATIC_COMPLEXITY)
        self.value = value

    def __add__(self, other):
        if not isinstance(other, MaxCyclomaticComplexityMetric):
            raise NotImplementedError
        return MaxCyclomaticComplexityMetric(max(self.value, other.value))

    def get(self) -> tuple[str, float]:
        '''
        Returns metric value.
        '''
        return MAX_CYCLOMATIC_COMPLEXITY, self.value

class MaxCyclomaticComplexityCalculator(ClangMetricCalculator):
    '''
    Calculates MAX_CYCLOMATIC_COMPLEXITY.
    '''

    def __call__(self, node: clang.cindex.Cursor) -> Metric:
        if not self.validate_cursor(node):
            return MaxCyclomaticComplexityMetric(0)
        return MaxCyclomaticComplexityMetric(_calculate_cyclomatic_complexity(node))

    def validate_cursor(self, cursor: clang.cindex.Cursor) -> bool:
        '''
        Validates that given cursor can be used for calculation 
        by this calculator in `__call__`.

        Returns:
        bool: can cursor be used for calculation or not.
        '''
        return is_definition_of_func_or_method(cursor)
