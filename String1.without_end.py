"""Python String 1 exercise 8.

http://codingbat.com/prob/p138533

Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

without_end('Hello') → 'ell' without_end('java') → 'av' without_end('coding') → 'odin'"""

def without_end(str):
  
    l = list(str)
    l[0] = ''
    l[len(str)-1] = ''
    s = ''.join(l)
    return s
