"""Python String 1 exercise 7.

http://codingbat.com/prob/p107010

Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

first_half('WooHoo') → 'Woo' first_half('HelloThere') → 'Hello' first_half('abcdef') → 'abc'"""

def first_half(str):
  
    l = list(str)
    half = l[:len(str)/2]
    s = ''.join(half)
    return s
