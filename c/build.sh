rm *.o
rm *.a
rm test_lexer

gcc -Wall -Wextra -o3 -c lexer.c -o lexer.o
gcc -Wall -Wextra -o3 test_lexer.c lexer.o -o test_lexer
