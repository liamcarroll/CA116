#!/usr/bin/env python

import sys

n = 20

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

m = (y2 - y1) / (x2 - x1)
c = y1 - m * x1

def should_plot(x,y):
   if x < x1 and x < x2:
      return False
   if x1 < x and x2 < x











print " " + "-" * n

i = 0
while i < n:
   y = n - i - 1
   output = []

   x = 0
   while x < n:
      if should_plot(x,y):
         output.append("*")
      else:
         output.append(" ")
      x += 1

   print "|" + "".join(output) + "|"
   i += 1

print " " + "-" * n
