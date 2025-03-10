'''
Module for NUMBER_OF_CLASSES metric.
'''

import clang.cindex

from cpp_stats.metrics.metric_calculator import Metric, ClangMetricCalculator

METRIC_NAME = 'NUMBER_OF_CLASSES'

class NumberOfClassesMetric(Metric):
    '''
    Represents NUMBER_OF_CLASSES metric.
    '''

    def __init__(self, value: int):
        '''
        Initializes metric.
        
        Parameters:
        value (float): Metric value.
        '''
        super().__init__(METRIC_NAME)
        self.value = value

    def __add__(self, other):
        if not isinstance(other, NumberOfClassesMetric):
            raise NotImplementedError
        return NumberOfClassesMetric(self.value + other.value)

    def get(self) -> tuple[str, float]:
        '''
        Returns metric value.
        '''
        return METRIC_NAME, self.value

class NumberOfClassesCalculator(ClangMetricCalculator):
    '''
    Calculates NUMBER_OF_CLASSES.
    '''

    def __call__(self, node: clang.cindex.Cursor) -> Metric:
        if node.kind != clang.cindex.CursorKind.CLASS_DECL or not node.is_definition():
            return NumberOfClassesMetric(0)
        return NumberOfClassesMetric(1)

    def observed_cursors(self) -> list[clang.cindex.CursorKind]:
        '''
        Returns list of cursor kinds that can be passed as an argument 
        for __call__.

        Returns:
        list[clang.cindex.CursorKind]: List of observed cursor kinds.
        '''
        return [clang.cindex.CursorKind.CLASS_DECL]
                