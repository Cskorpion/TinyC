import tempfile, os, pytest
from tinyc_lexer import Lexer
from tinyc_token import *

MODE = 0

def _make_tempfile_with_content(content):
    tfile = tempfile.NamedTemporaryFile(delete=False).name
    with open(tfile, "w") as f:
        f.write(content)
    return tfile

def _delete_tempfile(fname):
    os.unlink(fname)

def test_lex_simple():
    s = "int i = 7;"
    c_file = _make_tempfile_with_content(s)

    lexer = Lexer()
    lexer.open_file(c_file)

    tokens = [lexer.next_token()]
    while not tokens[-1].ttype == TOKEN_EOF:
        tokens.append(lexer.next_token())
        
    assert tokens[0].ttype == TOKEN_INT
    assert tokens[1].ttype == TOKEN_WHITESPACE   
    assert tokens[2].ttype == TOKEN_IDENT
    assert tokens[3].ttype == TOKEN_WHITESPACE
    assert tokens[4].ttype == TOKEN_EQUAL
    assert tokens[5].ttype == TOKEN_WHITESPACE
    assert tokens[6].ttype == TOKEN_NUMBER
    assert tokens[7].ttype == TOKEN_SEMICOL

    _delete_tempfile(c_file)

def test_lex_simple_wrong():
    s = "double d = 4.2"
    c_file = _make_tempfile_with_content(s)

    lexer = Lexer()
    lexer.open_file(c_file)

    with pytest.raises(Exception):
        lexer.next_token()

    _delete_tempfile(c_file)

