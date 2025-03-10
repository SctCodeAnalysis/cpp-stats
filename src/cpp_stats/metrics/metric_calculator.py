'''
Base classes for metrics and calculators.
'''

from pathlib import Path

import clang.cindex

class Metric:
    '''
    Class that stores metric name and value.
    '''

    def __init__(self, name):
        self._name = name

    def __add__(self, other):
        pass

    def get(self):
        '''
        Returns metric value. Should be called since metric can be summarization of many files,
        namespaces, classes and etc.
        '''

    def name(self):
        '''
        Returns name of metric.
        '''
        return self._name

class BasicMetricCalculator:
    '''
    Class for calculating specific metric.
    '''

    def __call__(self, file_paths: list[Path]) -> Metric:
        '''
        Calculates metric for a given set of C/C++ files.

        Parameters:
        file_paths (list[Path]): paths to C/C++ files

        Returns:
        Metric: Metrics calculated for set of files.
        '''

class ClangMetricCalculator:
    '''
    Class for calculating specific metric.
    '''

    def __call__(self, node: clang.cindex.Cursor) -> Metric:
        '''
        Calculates metric for a given node that represents function, 
        method, class or etc.

        Parameters:
        node (clang.cindex.Cursor): Node for which metric is 
        calculated.

        Returns:
        Metric: Metrics calculated for node.
        '''

    def observed_cursors(self) -> list[clang.cindex.CursorKind]:
        '''
        Returns list of cursor kinds that can be passed as an argument 
        for __call__.

        Returns:
        list[clang.cindex.CursorKind]: List of observed cursor kinds.
        '''
