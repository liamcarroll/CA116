#!/usr/bin/env python

words = []

line = raw_input()
while line != "end":
   words.append(line)
   line = raw_input()

s = ""

line = raw_input()
while line != "end":
   if 0 < len(line):
      s += (words[int(line)] + " ")
   else:
       s = s[:-1] + "\n"
   line = raw_input()

if 0 < len(s):
   print s[:-1]
