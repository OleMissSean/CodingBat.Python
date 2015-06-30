"""Python String 1 exercise 3.

http://codingbat.com/prob/p132290

The web is built with HTML strings like "Yay" which draws Yay as italic text. In this example, the "i" tag makes and which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "Yay".

make_tags('i', 'Yay') → 'Yay' make_tags('i', 'Hello') → 'Hello' make_tags('cite', 'Yay') → 'Yay'"""


def make_tags(tag, word):
  
    return ('<' + tag + '>' + word + '</' + tag + '>')
