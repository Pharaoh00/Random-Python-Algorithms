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

from collections import Counter
import re

sentence="Deidre paced on the beach behind her bungalow, unable to do anything but lecture herself over and over about how stupid she was to sleep with some random stranger."
sentence = "".join(sentence.split())
# for x in t:
#     print(Counter(re.findall(r'{}'.format(x), txt)))

for i, j in zip(sentence[::2], sentence[1::2]):
    pairs = i+j
    print(Counter(re.findall(r'{}'.format(pairs), sentence)))
