#!/usr/bin/env python

j = ""

s = raw_input()
while s != "END":
   j += (s[0] * int(s[2]))
   s = raw_input()

print j
