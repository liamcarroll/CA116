#!/usr/bin/env python

import secret_number

def play():

   low = 0
   mid = 500
   high = 999
   response = secret_number.guess(mid)

   while response != "correct":
      if response == "too-low":
         low = mid

      elif response == "too-high":
         high = mid

      mid = low + ((high - low) / 2)

      response = secret_number.guess(mid)

def main():
   print play()

if __name__ == "__main__":
   main()
