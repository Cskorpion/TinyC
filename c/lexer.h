#ifndef LEXER_H
#define LEXER_H

extern int TOKEN_ERROR;
extern int TOKEN_WHITESPACE;
extern int TOKEN_INT;

struct Token
{
    char* value;
    int type;
    int pos;
};

void set_text(char* text);

void set_pos(int p);

struct Token next_token(void);

#endif