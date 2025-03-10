from pathlib import Path

import pytest

import utils.clang

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

@pytest.fixture
def clang_index():
    '''
    Initializes Clang using environment variable `LIBCLANG_LIBRARY_PATH`
    '''
    yield utils.clang.clang_index()
