rm *.o
rm test_lexer

gcc -Wall -Wextra -o3 -c lexer.c -o lexer.o
gcc -Wall -Wextra -o3 test_lexer.c lexer.o -o test_lexer

./test_lexer

if [[ $? -eq 1 ]]; then
    echo "Lexer tests ok"
else
    echo "Lexer tests failed"
    exit
fi
