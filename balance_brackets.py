#!/bin/python3

# Balance Brackets
# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    open_brackets = []

    b_open = ["{", "(", "[" ]
    b_close = ["}", ")", "]" ]

    brackets = {
        ")": "(",
        "}": "{",
        "]": "["
        }

    def eval_b(b_open):
        if len(open_brackets) == 0:
            return "NO"
        last = open_brackets.pop()
        if b_open != last:
            return "NO"

    for b in s:
        if b in b_open:
            open_brackets.append(b)

        elif b in b_close:
            b_op = brackets[b]
            x = eval_b(b_op)
            if x:
                return x

    if len(open_brackets) == 0:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
