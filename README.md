# Repository Coverage

[Full report](https://htmlpreview.github.io/?https://github.com/SctCodeAnalysis/cpp-stats/blob/python-coverage-comment-action-data/htmlcov/index.html)

| Name                                          |    Stmts |     Miss |   Cover |   Missing |
|---------------------------------------------- | -------: | -------: | ------: | --------: |
| src/cpp\_stats/\_\_init\_\_.py                |        0 |        0 |    100% |           |
| src/cpp\_stats/analyzer.py                    |       28 |        5 |     82% | 34-37, 49 |
| src/cpp\_stats/ast/ast\_tree.py               |       19 |       14 |     26% |22-31, 39-48 |
| src/cpp\_stats/cpp\_stats.py                  |       31 |       11 |     65% |61, 70, 81-84, 91-93, 96, 110 |
| src/cpp\_stats/file\_sieve.py                 |       59 |        0 |    100% |           |
| src/cpp\_stats/metrics/\_\_init\_\_.py        |        0 |        0 |    100% |           |
| src/cpp\_stats/metrics/lines\_of\_code.py     |       21 |        0 |    100% |           |
| src/cpp\_stats/metrics/metric\_calculator.py  |       15 |        2 |     87% |    18, 30 |
| src/cpp\_stats/metrics/number\_of\_classes.py |       20 |        4 |     80% | 43-45, 55 |
| tests/clang/test\_ast\_tree.py                |       14 |        6 |     57% |     15-22 |
| tests/clang/test\_number\_of\_classes.py      |       46 |       26 |     43% |30-44, 51-65 |
| tests/conftest.py                             |       40 |        1 |     98% |        70 |
| tests/test\_analyzer.py                       |       26 |        0 |    100% |           |
| tests/test\_cpp\_stats.py                     |       22 |        0 |    100% |           |
| tests/test\_file\_sieve.py                    |       64 |        0 |    100% |           |
| tests/test\_lines\_of\_code.py                |       38 |        0 |    100% |           |
| tests/test\_sample.py                         |        4 |        0 |    100% |           |
| tests/utils/\_\_init\_\_.py                   |        1 |        0 |    100% |           |
| tests/utils/asserts.py                        |        2 |        0 |    100% |           |
| tests/utils/clang.py                          |       11 |        2 |     82% |     14-15 |
|                                     **TOTAL** |  **461** |   **71** | **85%** |           |


## Setup coverage badge

Below are examples of the badges you can use in your main branch `README` file.

### Direct image

[![Coverage badge](https://raw.githubusercontent.com/SctCodeAnalysis/cpp-stats/python-coverage-comment-action-data/badge.svg)](https://htmlpreview.github.io/?https://github.com/SctCodeAnalysis/cpp-stats/blob/python-coverage-comment-action-data/htmlcov/index.html)

This is the one to use if your repository is private or if you don't want to customize anything.

### [Shields.io](https://shields.io) Json Endpoint

[![Coverage badge](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/SctCodeAnalysis/cpp-stats/python-coverage-comment-action-data/endpoint.json)](https://htmlpreview.github.io/?https://github.com/SctCodeAnalysis/cpp-stats/blob/python-coverage-comment-action-data/htmlcov/index.html)

Using this one will allow you to [customize](https://shields.io/endpoint) the look of your badge.
It won't work with private repositories. It won't be refreshed more than once per five minutes.

### [Shields.io](https://shields.io) Dynamic Badge

[![Coverage badge](https://img.shields.io/badge/dynamic/json?color=brightgreen&label=coverage&query=%24.message&url=https%3A%2F%2Fraw.githubusercontent.com%2FSctCodeAnalysis%2Fcpp-stats%2Fpython-coverage-comment-action-data%2Fendpoint.json)](https://htmlpreview.github.io/?https://github.com/SctCodeAnalysis/cpp-stats/blob/python-coverage-comment-action-data/htmlcov/index.html)

This one will always be the same color. It won't work for private repos. I'm not even sure why we included it.

## What is that?

This branch is part of the
[python-coverage-comment-action](https://github.com/marketplace/actions/python-coverage-comment)
GitHub Action. All the files in this branch are automatically generated and may be
overwritten at any moment.