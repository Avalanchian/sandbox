#!/usr/bin/env python3

from sys import exit


def fizzbuzz(final, mul1=3, mul2=5):
    """Plays fizzbuzz using mul1 and mul2 as multiples up to final."""
    
    if final == 0:
        exit()
    else:
        for i in range(1, final +1):
            if (i % mul1 == 0) and (i % mul2 == 0):
                print("Fizzbuzz")
            elif i % mul1 == 0:
                print("Fizz")
            elif i % mul2 == 0:
                print("Buzz")
            else:
                print(i)


while True:
    try:
        fizzbuzz(int(input("Play until what number? Type 0 to quit.\n> ")))
    except ValueError:
        print("Must input an integer in numeral form (5 not five).")
