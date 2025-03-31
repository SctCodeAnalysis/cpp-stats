'''
Module for MEAN_COGNITIVE_COMPLEXITY and MAX_COGNITIVE_COMPLEXITY metrics.
'''

import clang.cindex

from cpp_stats.metrics.metric_calculator import Metric, ClangMetricCalculator

MEAN_COGNITIVE_COMPLEXITY = 'MEAN_COGNITIVE_COMPLEXITY'
MAX_COGNITIVE_COMPLEXITY = 'MAX_COGNITIVE_COMPLEXITY'

def __need_to_increase_value(node_kind: clang.cindex.CursorKind):
    return node_kind in [
        clang.cindex.CursorKind.IF_STMT,
        clang.cindex.CursorKind.WHILE_STMT,
        clang.cindex.CursorKind.FOR_STMT,
        clang.cindex.CursorKind.SWITCH_STMT
    ]

def __need_to_increase_depth(node_kind: clang.cindex.CursorKind):
    return node_kind in [
        clang.cindex.CursorKind.IF_STMT,
        clang.cindex.CursorKind.WHILE_STMT,
        clang.cindex.CursorKind.FOR_STMT,
        clang.cindex.CursorKind.SWITCH_STMT,
        clang.cindex.CursorKind.LAMBDA_EXPR,
    ]

def __is_break_linear_flow(node_kind: clang.cindex.CursorKind):
    return node_kind in [
        clang.cindex.CursorKind.CONTINUE_STMT,
        clang.cindex.CursorKind.BREAK_STMT,
        clang.cindex.CursorKind.GOTO_STMT,
        clang.cindex.CursorKind.CXX_CATCH_STMT,
    ]

def _calculate_cognitive_complexity(node: clang.cindex.Cursor, depth = 0) -> int:
    complexity = 1 if __is_break_linear_flow(node.kind) else 0
    for child in node.get_children():
        if __need_to_increase_value(child.kind):
            complexity += depth + 1
        complexity += _calculate_cognitive_complexity(
            child,
            depth + (1 if __need_to_increase_depth(child.kind) else 0)
        )
    return complexity

class MeanCognitiveComplexityMetric(Metric):
    '''
    Represents MEAN_COGNITIVE_COMPLEXITY metric.
    '''

    def __init__(self, sum_value: int, cnt: int):
        '''
        Initializes metric.
        
        Parameters:
        sum_value (int): sum of cognitive complexity values. 
        cnt (int): quantity of viewed functions, methods and lambdas.
        '''
        super().__init__(MEAN_COGNITIVE_COMPLEXITY)
        self.sum_value = sum_value
        self.cnt = cnt

    def __add__(self, other):
        if not isinstance(other, MeanCognitiveComplexityMetric):
            raise NotImplementedError
        return MeanCognitiveComplexityMetric(self.sum_value + other.sum_value, other.cnt + self.cnt)

    def get(self) -> tuple[str, float]:
        '''
        Returns metric value.
        '''
        value = 0
        if self.cnt != 0:
            value = self.sum_value / self.cnt
        return MEAN_COGNITIVE_COMPLEXITY, value

class MeanCognitiveComplexityCalculator(ClangMetricCalculator):
    '''
    Calculates MEAN_NUMBER_OF_METHODS_PER_CLASS.
    '''

    def __call__(self, node: clang.cindex.Cursor) -> Metric:
        if not self.validate_cursor(node):
            return MeanCognitiveComplexityMetric(0, 0)
        return MeanCognitiveComplexityMetric(_calculate_cognitive_complexity(node), 1)

    def validate_cursor(self, cursor: clang.cindex.Cursor) -> bool:
        '''
        Validates that given cursor can be used for calculation 
        by this calculator in `__call__`.

        Returns:
        bool: can cursor be used for calculation or not.
        '''
        return (
            cursor.kind in [
                clang.cindex.CursorKind.CXX_METHOD,
                clang.cindex.CursorKind.FUNCTION_DECL
            ]
            and cursor.is_definition()
        )

class MaxCognitiveComplexityMetric(Metric):
    '''
    Represents MAX_COGNITIVE_COMPLEXITY metric.
    '''

    def __init__(self, value: int):
        '''
        Initializes metric.
        
        Parameters:
        value (int): cognitive complexity value.
        '''
        super().__init__(MAX_COGNITIVE_COMPLEXITY)
        self.value = value

    def __add__(self, other):
        if not isinstance(other, MaxCognitiveComplexityMetric):
            raise NotImplementedError
        return MaxCognitiveComplexityMetric(max(self.value, other.value))

    def get(self) -> tuple[str, float]:
        '''
        Returns metric value.
        '''
        return MAX_COGNITIVE_COMPLEXITY, self.value

class MaxCognitiveComplexityCalculator(ClangMetricCalculator):
    '''
    Calculates MAX_NUMBER_OF_METHODS_PER_CLASS.
    '''

    def __call__(self, node: clang.cindex.Cursor) -> Metric:
        if not self.validate_cursor(node):
            return MaxCognitiveComplexityMetric(0)
        return MaxCognitiveComplexityMetric(_calculate_cognitive_complexity(node))

    def validate_cursor(self, cursor: clang.cindex.Cursor) -> bool:
        '''
        Validates that given cursor can be used for calculation 
        by this calculator in `__call__`.

        Returns:
        bool: can cursor be used for calculation or not.
        '''
        return (
            cursor.kind in [
                clang.cindex.CursorKind.CXX_METHOD,
                clang.cindex.CursorKind.FUNCTION_DECL
            ]
            and cursor.is_definition()
        )
