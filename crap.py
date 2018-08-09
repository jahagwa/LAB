#!/usr/bin/python3.6

import sys

print('Give me a basic expression')
expression = float(eval(input()))
print('Give me the answer to the expression')
answer = float(input())
if expression == answer:
    print('Thats right')
    sys.exit()
elif expression != answer:
    print('Thats wrong')
    sys.exit()
