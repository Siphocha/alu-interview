#!/usr/bin/python3
"""Calculates the fewest number of operations needed
to result in exactly n 'H' characters in the file."""


def minOperations(n):
    """
    Calculate the minimum number of operations to achieve n
    'H' characters in the file."""
    # IF n less than or equal to 1 its impossible for anything
    if n <= 1:
        return 0

    # Start counting amount of times
    amount = 0

    # Iterate through starting from 2
    Num = 2
    while Num * Num <= n:
        while n % Num == 0:
            # Do Copy All and Paste operations ONLY IF DIVISIBLE
            amount += Num
            n /= Num
        Num += 1
    # n is greater than 1, it is correct.
    if n > 1:
        amount += int(n)
    return amount
