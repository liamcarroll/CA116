#!/usr/bin/env python

import sys

n = int(sys.argv[1])

i = 1
while i <= n:
   print " " * ((n - i) / 2) + "*" * i
   i += 2

i = n - 2
while 0 < i:
   print " " * ((n - i) / 2) + "*" * i
   i -= 2
