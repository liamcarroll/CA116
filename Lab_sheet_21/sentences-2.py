#!/usr/bin/env python

import sys
words = sys.stdin.read().split()

def is_terminator(word):
   return word[-1] in [".", "?", "!"]

i = 0
while i < len(words):
   j = i
   while j < len(words) and not is_terminator(words[j]):
      j += 1

   j += 1
   words[i] = words[i].capitalize()
   print " ".join(words[i:j])

   i = j