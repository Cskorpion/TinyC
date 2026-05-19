
TOKEN_ERROR = 0
TOKEN_WHITESPACE = 1
TOKEN_PARAOPEN = 2
TOKEN_PARACLOSE = 3
TOKEN_BRAOPEN = 4
TOKEN_BRACLOSE = 5
TOKEN_SEMICOL = 6
TOKEN_EQUAL = 7
TOKEN_SMALLER = 8
TOKEN_GREATER = 9
TOKEN_PLUS = 10
TOKEN_MINUS = 11
TOKEN_INT = 12
TOKEN_IDENT = 13
TOKEN_IF = 14
TOKEN_ELSE = 15
TOKEN_WHILE = 16
TOKEN_DO = 17
TOKEN_NUMBER = 18
TOKEN_EOF = 19

TOKEN_NAMES = ["ERROR", "WHITESPACE", "PARAOPEN", "PARACLOSE", "BRAOPEN",
               "BRACLOSE", "SEMICOL", "EQUAL", "SMALLER", "GREATER", "PLUS",
               "MINUS", "INT", "IDENT", "IF", "ELSE", "WHILE", "DO", "NUMBER", "EOF"]

class Token(object):
    ttype = TOKEN_ERROR
    tvalue = ""
    tpos = -1

    def __init__(self, typ, val=None, pos=None):
        self.ttype = typ
        self.tvalue = val
        self.tpos = pos
    
    @staticmethod
    def _id_to_name(id):
        if id > len(TOKEN_NAMES)-1: return "UNKNOWN"
        return TOKEN_NAMES[id]
    
    def get_str(self):
        return "TOKEN_%s_VALUE_[%s]_POS_[%d]" % (Token._id_to_name(self.ttype), self.tvalue, self.tpos)

    def __str__(self):
        return "TOKEN_%s_VALUE_[%s]_POS_[%d]" % (Token._id_to_name(self.ttype), self.tvalue, self.tpos)
    
    def __repr__(self):
        return str(self)