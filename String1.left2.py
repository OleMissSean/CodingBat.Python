"""Python String 1 exercise 11.

http://codingbat.com/prob/p160545

Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

left2('Hello') → 'lloHe' left2('java') → 'vaja' left2('Hi') → 'Hi'"""

def left2(str):
    
    if(len(str) >= 2):
        l = list(str)
        first, last = l[0:2], l[2:]
        s = ''.join(last) + ''.join(first)
        return s
    else:
        return str
