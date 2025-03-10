'''
Main class for calculating metrics.
'''

from pathlib import Path
import clang.cindex

from cpp_stats.metrics.lines_of_code import LinesOfCodeCalculator
from cpp_stats.metrics.number_of_classes import NumberOfClassesCalculator
from cpp_stats.metrics.metric_calculator import Metric
from cpp_stats.ast.ast_tree import analyze_ast

class CodeAnalyzer:
    '''
    Provides calculated metrics.
    '''

    def __init__(self, c_cxx_files: list[Path], clang_path: str = None):
        self._files = c_cxx_files
        self._ast_tree = None
        self._basic_calculators = {
            'LINES_OF_CODE' : LinesOfCodeCalculator(),
        }
        self._clang_calculators = {
            'NUMBER_OF_CLASSES' : NumberOfClassesCalculator(),
        }
        self._cache = {
            'LINES_OF_CODE' : None,
            'NUMBER_OF_CLASSES' : None,
        }
        self._clang_cache = None
        self._use_clang = False
        if clang_path is not None:
            self._use_clang = True
            clang.cindex.Config.set_library_file(clang_path)
            index = clang.cindex.Index.create()
            self._clang_cache = analyze_ast(index, c_cxx_files, self._clang_calculators)

    def metric(self, metric_name: str) -> Metric | None:
        '''
        Returns calculated metric by name.
        
        Parameters:
        metric_name (str): Metric name.
        '''
        if self._cache.get(metric_name, None) is not None:
            return self._cache[metric_name]
        if self._use_clang and self._clang_cache.get(metric_name, None) is not None:
            return self._clang_cache[metric_name]
        if self._basic_calculators.get(metric_name, None) is not None:
            self._cache[metric_name] = self._basic_calculators[metric_name](self._files)
        return self._cache.get(metric_name, None)
