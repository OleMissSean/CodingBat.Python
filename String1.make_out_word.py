"""Python String 1 exercise 4.

http://codingbat.com/prob/p129981

Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<>".

make_out_word('<<>>', 'Yay') → '<>' make_out_word('<<>>', 'WooHoo') → '<>' make_out_word('[[]]', 'word') → '[[word]]'"""

def make_out_word(out, word):
  
    str = list(out)
    first, second = str[:len(out)/2], str[len(out)/2:]
    f = ''.join(first)
    s = ''.join(second)
    return(f + word + s)
