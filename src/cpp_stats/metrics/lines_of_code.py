'''
Module for LINES_OF_CODE metric.
'''

from pathlib import Path

from cpp_stats.metrics.metric_calculator import Metric, BasicMetricCalculator

METRIC_NAME = 'LINES_OF_CODE'

class LinesOfCodeMetric(Metric):
    '''
    Represents LINES_OF_CODE metric.
    '''
    def __init__(self, value: float):
        '''
        Initializes metric.
        
        Parameters:
        value (float): Metric value.
        '''
        super().__init__(METRIC_NAME)
        self.value = value

    def __add__(self, other):
        if not isinstance(other, LinesOfCodeMetric):
            raise NotImplementedError
        return LinesOfCodeMetric(self.value + other.value)

    def get(self) -> tuple[str, float]:
        '''
        Returns metric value.
        '''
        return METRIC_NAME, self.value


class LinesOfCodeCalculator(BasicMetricCalculator):
    '''
    Calculates LINES_OF_CODE.
    '''

    def __call__(self, file_paths: list[Path]) -> Metric:
        cnt = 0
        for file_path in file_paths:
            with open(file_path, 'r') as f:
                while f.readline():
                    cnt += 1
        return LinesOfCodeMetric(cnt)
                