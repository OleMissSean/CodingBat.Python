"""Python String 1 exercise 5.

http://codingbat.com/prob/p148853

Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string length will be at least 2.

extra_end('Hello') → 'lololo' extra_end('ab') → 'ababab' extra_end('Hi') → 'HiHiHi'"""

def extra_end(str):
  
    l = list(str)
    l = l[len(str)-2:]
    s = ''.join(l)
    return s + s + s
