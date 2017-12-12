#!/usr/bin/env python

start = []

line = raw_input()
while line != "end":
   start.append(int(line))
   line = raw_input()

most_amount = 0

i = 0
while i < len(start):
   servers = 0
   j = i
   while j < len(start) and start[j] < start[i] + 1000:
      servers += 1
      j += 1

   if most_amount < servers:
      most_amount = servers
   i += 1

print most_amount
