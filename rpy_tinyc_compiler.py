from tinyc_lexer import Lexer
from tinyc_parser import Parser
from tinyc_token import TOKEN_EOF

def entry_point_lex(argv):
    tokens = []
    lexer = Lexer()

    lexer.open_file(argv[1])
    
    max_console_steps = 2**32 - 1

    while max_console_steps != 0: # rpy wants main loop to be finite
        max_console_steps -= 1

        # TODO: replace this with stdin read

        nxt_tkn = lexer.next_token()
        if not nxt_tkn or nxt_tkn.ttype == TOKEN_EOF:
            break
        tokens.append(nxt_tkn)
    
    for token in tokens:
        print token.get_str()
    
    lexer.close_file()
    
    return 0

def entry_point_parse(argv):
    lexer = Lexer()
    lexer.open_file(argv[1])
    parser = Parser(lexer)
    ast = parser.parse()
    import pdb; pdb.set_trace()
    lexer.close_file()
    return 0

def target(*args):
    return entry_point_lex

# This is for executing on cpy/pypy - remove when translating
from sys import argv
#print "lexing"
#entry_point_lex(argv)
#print "parsing"
#entry_point_parse(argv)