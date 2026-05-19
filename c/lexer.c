#include "lexer.h"
#include <string.h>

static char* input;
static int pos = 0;

int TOKEN_ERROR = 0;
int TOKEN_WHITESPACE = 1;
int TOKEN_INT = 2;

void set_text(char* text) {
    input = text;
}

void set_pos(int p) { 
    pos = p;
}

struct Token next_token(void) {
    int pos = 0;

    struct Token t;
    t.pos = pos;

    if(input[pos] == ' ') {
        t.type = TOKEN_WHITESPACE;
    } elif(strcmp(strcpy(), "if"))
    
    else {
        t.type = TOKEN_ERROR;
    }
    
    return t;
}