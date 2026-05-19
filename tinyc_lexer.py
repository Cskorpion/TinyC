from tinyc_token import *
import os

class Lexer(object):

    def __init__(self):
        self.pos = 0
        self.fd = -1
        self.curchar = None
        self.outlook = []

    def open_file(self, path):
        # should the lexer take care of opening a file???
        self.fd = os.open(path, os.O_RDONLY, 511)
    
    def close_file(self):
        os.close(self.fd)

    def _read_next_char(self):
        self.pos += 1
        return str(os.read(self.fd, 1))
    
    def peek(self):
        if len(self.outlook) != 0: return self.outlook[-1]
        tok = self.next_token()
        self.outlook.append(tok)
        return tok
    
    def next_token(self):
        if len(self.outlook) != 0: return self.outlook.pop()

        if not self.curchar == ";": # hacky: without lookahead I must consume the character that previously ended the loop reading lower down
            self.curchar = self._read_next_char()

        # character leftover from prev. incovation can only be a semicolon
        if self.curchar == ";":  self.curchar = ""; return Token(TOKEN_SEMICOL, None, self.pos)   
        # normally check for characters here
        elif self.curchar == "":   return Token(TOKEN_EOF, None, self.pos)
        elif self.curchar == "(":  return Token(TOKEN_PARAOPEN, None, self.pos)
        elif self.curchar == ")":  return Token(TOKEN_PARACLOSE, None, self.pos)
        elif self.curchar == "{":  return Token(TOKEN_BRAOPEN, None, self.pos)
        elif self.curchar == "}":  return Token(TOKEN_BRACLOSE, None, self.pos)
        elif self.curchar == ";":  return Token(TOKEN_SEMICOL, None, self.pos)
        elif self.curchar == "=":  return Token(TOKEN_EQUAL, None, self.pos)
        elif self.curchar == "<":  return Token(TOKEN_SMALLER, "<", self.pos)        
        elif self.curchar == ">":  return Token(TOKEN_GREATER, ">", self.pos)
        elif self.curchar == "+":  return Token(TOKEN_PLUS, "+", self.pos)        
        elif self.curchar == "-":  return Token(TOKEN_MINUS, "-", self.pos)
        else:
            start_pos = self.pos # save 'real' start pos
            wrd = self.curchar

            # read all consecutive chars until whitespace, eof or semicolon
            # problem the 'stopping' character must still be consumed normally in the next invocation of next_token()
            while True:
                nxt = self._read_next_char()
                if nxt == " " or nxt == "" or nxt == ";":
                    self.curchar = nxt
                    break
                wrd += nxt

            # check some keywords
            if wrd == "if":      return Token(TOKEN_IF, None, start_pos)
            elif wrd == "do":    return Token(TOKEN_DO, None, start_pos)
            elif wrd == "else":  return Token(TOKEN_ELSE, None, start_pos)
            elif wrd == "while": return Token(TOKEN_WHILE, None, start_pos)
            elif wrd == "int":   return Token(TOKEN_INT, None, start_pos)
            
            # check if wrd is an int
            try:
                intval = int(wrd)
                return Token(TOKEN_INT, str(intval), start_pos)
            except Exception as e:
                pass     

            # must be an identifier now
            assert len(wrd) == 1

            return Token(TOKEN_IDENT, str(wrd), start_pos)