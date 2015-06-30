"""Python Warmup 1 exercise 11.

http://codingbat.com/

Given a string, return a new string where the first and last chars have been exchanged.

front_back('code') → 'eodc' front_back('a') → 'a' front_back('ab') → 'ba'"""

def front_back(str):
  
    l = list(str)
    l[:1], l[-1:] = l[-1:], l[:1]
    str2 = ''.join(l)
    return str2
