'''
Module for helper functions
'''

import clang.cindex

def mangle_cursor_name(node: clang.cindex.Cursor) -> str:
    '''
    Returns string that contains full name of node with parent classes, namespaces and etc.
    
    Example:
    `::ThreeDRenderer::Camera`
    
    Parameters:
    node (clang.cindex.Cursor): cursor for which mangled name is being calculated.
    '''
    if node.kind == clang.cindex.CursorKind.TRANSLATION_UNIT:
        return ""
    return mangle_cursor_name(node.semantic_parent) + '::' + node.displayname

def is_definition_of_func_or_method(node: clang.cindex.Cursor) -> bool:
    '''
    Says whether node is definition of function or method or not.
    
    
    Parameters:
    node (clang.cindex.Cursor): cursor to check.
    '''
    return (
        node.kind in [
            clang.cindex.CursorKind.CXX_METHOD,
            clang.cindex.CursorKind.FUNCTION_DECL
        ]
        and node.is_definition()
    )
