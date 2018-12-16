#!/usr/bin/env python
#-*- coding:utf-8 -*-
# ----------------------------------------------------------- #
# Filename: findPairs.py
# Creation Date: sexta-feira, 14 dezembro 2018 10:51
# Author: Hamon-Rá Taveira Guimarães
# Contact:
#         GitHub: https://github.com/
#         E-mail: hamoncsl@hotmail.com
#         Facebook: https://www.facebook.com/hamonra.taveira
# ----------------------------------------------------------- #

# This example i'ill find all the pairs on a sentence, and count them.
# If you need more than a pair, you can look at grouper() function on itertools recipes pydoc
# This example does handle the whitespaces properly. The example just join all.
# If you needed, you can make some function to handle the wthitespaces, with the grouper()
# you can make something to "see" what's is the next:
# For example, on this sequence ("Deidre paced"):
# You can ask for grouper() to pick 3 letters, the function i'll return:
# [("D, "e", "i"), ("d", "r", "e"), (" ", "p", "a"), ("c", "e", "d")]
# And you can think of a way to handle things properly, "de", "ei", "dre", "pa", "ced"... Something like that.
# Btw, i'm not a native english speark. I'm thinking how things have to be, out of my head.

from collections import Counter
import itertools

# Sentence from https://sentence.yourdictionary.com/random
sentence="Deidre paced on the beach behind her bungalow, unable to do anything but lecture herself over and over about how stupid she was to sleep with some random stranger."
sentence = "".join(sentence.split())

# Example by itertools recipe on python doc: https://docs.python.org/3/library/itertools.html#itertools-recipes
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

# Example by alkasm on reddit post: https://www.reddit.com/r/Python/comments/a6aug3/a_finder_and_counter_pairs_on_sentence/
print(dict(Counter(map(''.join, pairwise(sentence)))))

# breaking things down:
# The pairwise i'll return tuples(pairs) of a sequence.
# For this examples i'll return:
# ("D", "e"), ("e", "i"), ("d", "r") ...
#
# Now we use map() for join ("D", "e") ... like that:
# De, ei, dr ...
#
# With Counter() we can count how many "de", "ei" "dr" are in the setence.
#
# And with dict, we convert the Counter thing to a more organize data, with keys and values.
