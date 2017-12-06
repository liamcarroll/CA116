#!/usr/bin/env/python

i = 0
while i < len(a):          #Iterate over a list a
   p = i                   #Make the assumption that value at the ith position is the smallest
   j = i + 1               
   while j < len(a):       #Iterate over the rest of the list (elements after i)
      if a[j] < a[p]:      #If any element is found to be smaller than i
         p = j             #Update the smallest value, p
      j += 1               #Iterating, the smallest value after i is found

   tmp = a[p]              #The smallest value found swaps with the value in the ith position
   a[p] = a[i]             
   a[i] = tmp

   i += 1                  #We iterate over the entire list until it is sorted

#Selection sort is O(n^2)
#Only practical on small-to-medium length (Up to a few thousand elements)
#On larger sequences (millions of elements): Selection sort is likely to be too slow because n^2 is too big
