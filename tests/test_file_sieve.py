'''
Tests module file_sieve.py
'''

from pathlib import Path
import pytest

import cpp_stats.file_sieve

def assert_lists_equal_unordered(expected, actual):
    '''
    Asserts that two lists contain same elements.
    
    Parameters:
    `expected` (list): Expected list.
    `actual` (list): List to check.
    '''
    assert sorted(expected) == sorted(actual), f"Expected: {expected}, Actual: {actual}"

def rename_git_ignore_and_modules(repo_path: Path, to_test: bool = True):
    '''
    Renames `test.gitignore` to `.gitignore` and 
    `test.gitmodules` to `.gitmodules` if `to_test == False` or
    renames `.gitignore` to `test.gitignore` and 
    `.gitmodules` to `test.gitmodules` if `to_test == True`
    '''
    if to_test:
        for entry in repo_path.rglob('.gitignore'):
            entry.rename(entry.parent.joinpath('test.gitignore'))
        for entry in repo_path.rglob('.gitmodules'):
            entry.rename(entry.parent.joinpath('test.gitmodules'))
    else:
        for entry in repo_path.rglob('test.gitignore'):
            entry.rename(entry.parent.joinpath('.gitignore'))
        for entry in repo_path.rglob('test.gitmodules'):
            entry.rename(entry.parent.joinpath('.gitmodules'))

@pytest.fixture
def repo():
    '''
    Returns path to test repository located at `/tests/data/repo`
    '''
    repo_path = Path('./tests/data/repo')
    rename_git_ignore_and_modules(repo_path, False)
    yield repo_path
    rename_git_ignore_and_modules(repo_path, True)

@pytest.fixture
def repo_with_gitignore():
    '''
    Returns path to test repository located at `/tests/data/repo_with_gitignore`
    '''
    repo_path = Path('./tests/data/repo_with_gitignore')
    rename_git_ignore_and_modules(repo_path, False)
    yield repo_path
    rename_git_ignore_and_modules(repo_path, True)

@pytest.fixture
def repo_with_2gitignore():
    '''
    Returns path to test repository located at `/tests/data/repo_with_2gitignore`
    '''
    repo_path = Path('./tests/data/repo_with_2gitignore')
    rename_git_ignore_and_modules(repo_path, False)
    yield repo_path
    rename_git_ignore_and_modules(repo_path, True)

@pytest.fixture
def repo_with_ignr_modules():
    '''
    Returns path to test repository located at `/tests/data/repo_with_ignr_modules`
    '''
    repo_path = Path('./tests/data/repo_with_ignr_modules')
    rename_git_ignore_and_modules(repo_path, False)
    yield repo_path
    rename_git_ignore_and_modules(repo_path, True)

def test_find_gitignore_1(repo: Path):
    '''
    Tests that in repository without `.gitignore`
    function `src.cpp_stats.file_sieve._locate_file`
    does not locate any `.gitignore` files
    '''
    file_to_locate = '.gitignore'
    expected = []

    actual = cpp_stats.file_sieve._locate_file(repo, file_to_locate, [])

    assert_lists_equal_unordered(expected, actual)

def test_find_gitignore_2(repo_with_gitignore: Path):
    '''
    Tests that in repository with `.gitignore`
    function `src.cpp_stats.file_sieve._locate_file` 
    finds exactly one `.gitignore` file.
    '''
    file_to_locate = '.gitignore'
    expected = [
        Path('./tests/data/repo_with_gitignore/.gitignore')
    ]

    actual = cpp_stats.file_sieve._locate_file(repo_with_gitignore, file_to_locate, [])

    assert_lists_equal_unordered(expected, actual)

def test_find_gitignore_3(repo_with_2gitignore: Path):
    '''
    Tests that in repository with `.gitignore`
    function `src.cpp_stats.file_sieve._locate_file` 
    finds exactly one `.gitignore`.
    '''
    file_to_locate = '.gitignore'
    expected = [
        Path('./tests/data/repo_with_2gitignore/.gitignore'),
        Path('./tests/data/repo_with_2gitignore/folder/.gitignore'),
    ]

    actual = cpp_stats.file_sieve._locate_file(repo_with_2gitignore, file_to_locate, [])

    assert_lists_equal_unordered(expected, actual)

def test_find_gitignore_with_banned_dir_1(repo_with_2gitignore: Path):
    '''
    Tests that in repository with banned directories and `.gitignore`
    function `src.cpp_stats.file_sieve._locate_file` 
    finds exactly one
    '''
    file_to_locate = '.gitignore'
    banned_dirs = [
        Path('./tests/data/repo_with_2gitignore/folder/')
    ]
    expected = [
        Path('./tests/data/repo_with_2gitignore/.gitignore'),
    ]

    actual = cpp_stats.file_sieve._locate_file(repo_with_2gitignore, file_to_locate, banned_dirs)

    assert_lists_equal_unordered(expected, actual)

def test_list_gitignore_dirs_1(repo_with_gitignore: Path):
    '''
    Tests that in repository with `.gitignore`
    function `src.cpp_stats.file_sieve._get_git_ignore_dirs` 
    finds all ignored dirs
    '''
    gitignore_path = repo_with_gitignore.joinpath('.gitignore')
    expected = [
        repo_with_gitignore.joinpath('ignored_dir/')
    ]

    actual = cpp_stats.file_sieve._get_git_ignore_dirs(gitignore_path)

    assert_lists_equal_unordered(expected, actual)

def test_list_gitignore_dirs_2(repo_with_2gitignore: Path):
    '''
    Tests that in repository with `.gitignore`
    function `src.cpp_stats.file_sieve._get_git_ignore_dirs`
    finds all ingored dirs.
    '''
    gitignore_path = repo_with_2gitignore.joinpath('.gitignore')
    expected = [
        repo_with_2gitignore.joinpath('ignored_dir')
    ]

    actual = cpp_stats.file_sieve._get_git_ignore_dirs(gitignore_path)

    assert_lists_equal_unordered(expected, actual)

def test_list_gitignore_dirs_3(repo_with_2gitignore: Path):
    '''
    Tests that in repository with nested `.gitignore`
    function `src.cpp_stats.file_sieve._get_git_ignore_dirs`
    finds all ingored dirs.
    '''
    gitignore_path = repo_with_2gitignore.joinpath('folder').joinpath('.gitignore')
    expected = [
        repo_with_2gitignore.joinpath('folder').joinpath('ignored_dir')
    ]

    actual = cpp_stats.file_sieve._get_git_ignore_dirs(gitignore_path)

    assert_lists_equal_unordered(expected, actual)

def test_list_git_modules_dirs_1(repo_with_ignr_modules: Path):
    '''
    Tests that in repository with `.gitmodules` 
    function `src.cpp_stats.file_sieve._get_git_modules_dirs`
    finds all submodules.
    '''
    gitmodules_path = repo_with_ignr_modules.joinpath('.gitmodules')
    expected = [
        repo_with_ignr_modules.joinpath('submodule1'),
        repo_with_ignr_modules.joinpath('submodule2')
    ]

    actual = cpp_stats.file_sieve._get_git_modules_dirs(gitmodules_path)

    assert_lists_equal_unordered(expected, actual)

def test_sieve_c_cxx_files_1(repo: Path):
    '''
    Tests that
    function `src.cpp_stats.file_sieve.sieve_c_cxx_files`
    finds all C/C++ files.
    '''
    expected = [
        repo.joinpath('main.cpp')
    ]

    actual = cpp_stats.file_sieve.sieve_c_cxx_files(repo)

    assert_lists_equal_unordered(expected, actual)

def test_sieve_c_cxx_files_2(repo_with_gitignore: Path):
    '''
    Tests that in repository with `.gitignore`
    function `src.cpp_stats.file_sieve.sieve_c_cxx_files`
    finds all not ignored C/C++ files.
    '''
    expected = [
        repo_with_gitignore.joinpath('main.cpp')
    ]

    actual = cpp_stats.file_sieve.sieve_c_cxx_files(repo_with_gitignore)

    assert_lists_equal_unordered(expected, actual)

def test_sieve_c_cxx_files_3(repo_with_2gitignore: Path):
    '''
    Tests that in repository with `.gitignore`
    function `src.cpp_stats.file_sieve.sieve_c_cxx_files`
    finds all not ignored C/C++ files.
    '''
    expected = [
        repo_with_2gitignore.joinpath('main.cpp')
    ]

    actual = cpp_stats.file_sieve.sieve_c_cxx_files(repo_with_2gitignore)

    assert_lists_equal_unordered(expected, actual)

def test_sieve_c_cxx_files_4(repo_with_ignr_modules: Path):
    '''
    Tests that in repository with `.gitignore` and `.gitmodules`
    function `src.cpp_stats.file_sieve.sieve_c_cxx_files`
    finds all not ignored C/C++ files.
    '''
    expected = [
        repo_with_ignr_modules.joinpath('main.cpp'),
        repo_with_ignr_modules.joinpath('src').joinpath('class.hpp'),
    ]

    actual = cpp_stats.file_sieve.sieve_c_cxx_files(repo_with_ignr_modules)

    assert_lists_equal_unordered(expected, actual)

def test_sieve_c_cxx_files_none():
    '''
    Tests that
    function `src.cpp_stats.file_sieve.sieve_c_cxx_files`
    return None when `repo_path` is None.
    '''
    expected = None

    actual = cpp_stats.file_sieve.sieve_c_cxx_files(None)

    assert expected == actual
