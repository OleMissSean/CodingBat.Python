"""Python String 1 exercise 6.

http://codingbat.com/prob/p184816

Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string is shorter than length 2, return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".

first_two('Hello') → 'He' first_two('abcdefg') → 'ab' first_two('ab') → 'ab'"""

def first_two(str):
  
    if(len(str) > 2):
        l = list(str)
        l = l[0:2]
        s = ''.join(l)
        return s
    else:
        return str
