#!/usr/bin/env python

import sys

n = 20

corner_x = int(sys.argv[1])
corner_y = int(sys.argv[2])
size = int(sys.argv[3])
plot = {}

i = 0
while i < size:
   #Bottom side
   key1 = str(corner_x + i) + "-" + str(corner_y)
   plot[key1] = True

   #Top side
   key2 = str(corner_x + i) + "-" + str(corner_y + (size - 1))
   plot[key2] = True

   #Left side
   key3 = str(corner_x) + "-" + str(corner_y + i)
   plot[key3] = True

   #Right side
   key4 = str(corner_x + (size - 1)) + "-" + str(corner_y + i)
   plot[key4] = True

   i += 1

def should_plot(x,y):   
   key = str(x) + "-" + str(y)
   
   if key in plot:
      return True
   else:
      return False


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
