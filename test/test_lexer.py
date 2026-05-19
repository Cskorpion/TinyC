import pytest
from tinyc_lexer import Lexer
from tinyc_token import *
from util import make_tempfile_with_content, delete_tempfile

MODE = 0

def test_lex_simple():
    s = "i = 7;"
    c_file = make_tempfile_with_content(s)

    lexer = Lexer()
    lexer.open_file(c_file)

    tokens = [lexer.next_token()]
    while not tokens[-1].ttype == TOKEN_EOF:
        tokens.append(lexer.next_token())
        
    assert tokens[0].ttype == TOKEN_IDENT
    assert tokens[1].ttype == TOKEN_EQUAL
    assert tokens[2].ttype == TOKEN_INT
    assert tokens[3].ttype == TOKEN_SEMICOL

    delete_tempfile(c_file)

def test_lex_simple_wrong():
    s = "d = 4.2"
    c_file = make_tempfile_with_content(s)

    lexer = Lexer()
    lexer.open_file(c_file)

    lexer.next_token() # read d
    lexer.next_token() # read =

    with pytest.raises(Exception):
        lexer.next_token() # read 4.2

    delete_tempfile(c_file)

