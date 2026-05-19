# TinyC

- For translating clone pypy (py2.7)
- adapt 'rpy_tinyc_compiler.py' to make it translatable (remove 'main' stuff)
- execute translate.sh
- run e.g. `rpy_tinyc_compiler-c inputfile.c`

- For executing on top of Python install cpy2.7 or pypy2.7
- adapt 'rpy_tinyc_compiler.py' to make it executable (uncomment 'main' stuff)
- run e.g. `pypy2.7 rpy_tinyc_compiler.py inputfile.c`