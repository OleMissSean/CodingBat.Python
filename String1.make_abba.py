"""Python String 1 exercise 2.

http://codingbat.com/prob/p182144

Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".

make_abba('Hi', 'Bye') → 'HiByeByeHi' make_abba('Yo', 'Alice') → 'YoAliceAliceYo' make_abba('What', 'Up') → 'WhatUpUpWhat'"""

def make_abba(a, b):
  
    return (a + b + b + a)
