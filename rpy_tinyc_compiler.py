from tinyc_lexer import Lexer
from tinyc_token import TOKEN_EOF

def entry_point_lex(argv):
    tokens = []
    lexer = Lexer()

    lexer.open_file(argv[1])
    
    max_console_steps = 2**32 - 1

    while max_console_steps != 0: # rpy wants main loop to be finite
        max_console_steps -= 1

        nxt_tkn = lexer.next_token()
        if not nxt_tkn or nxt_tkn.ttype == TOKEN_EOF:
            break
        tokens.append(nxt_tkn)
    
    for token in tokens:
        print token.get_str()
    
    return 0

def entry_point_parse(argv):
    return 0

def target(*args):
    return entry_point_lex

# This is for executing on cpy/pypy - remove when translating
#from sys import argv
#entry_point_lex(argv)

