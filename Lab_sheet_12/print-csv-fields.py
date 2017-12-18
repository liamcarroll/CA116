#!/usr/bin/env python

a =[]

line = raw_input()
while line != "end":
   line = line.split(",")
   a.append(line)
   line = raw_input()

n = input()

i = 0
while i < len(a):
   print a[i][n]
   i += 1
