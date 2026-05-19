#include "lexer.h"
#include <assert.h>
#include <stdio.h>


int test_lexer_simple(void) {
    set_text("int i = 7;");
    set_pos(0);

    struct Token t0 = next_token();
    assert(t0.type == TOKEN_INT);
    
    struct Token t1 = next_token();
    struct Token t2 = next_token();
    struct Token t3 = next_token();
    struct Token t4 = next_token();
    struct Token t5 = next_token();
    struct Token t6 = next_token();
    struct Token t7 = next_token();
    struct Token t8 = next_token();

    printf("fdg\n");
    return 0;
}

int main(void) {

    test_lexer_simple();

    return 0;
}