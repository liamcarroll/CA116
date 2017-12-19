#!/usr/bin/env python

import sys
import math

#Binary operators.

def add(x,y):
   return x + y

def sub(x,y):
   return x - y

def mul(x,y):
   return x * y

def div(x,y):
   return x / y

def rem(x, y):
   return x % y

def power(x,y):
   return x ** y

binary = {
   "+": add,
   "-": sub,
   "*": mul,
   "/": div,
   "%": rem,
   "**": power,
}

#Unary operators.

def neg(x):
   return -x

def sqr(x):
   return x * x

def sqrt(x):
   return math.sqrt(x)

def log(x):
   return math.log(x)

unary = {
   "n": neg,
   "s": sqr,
   "r": sqrt,
   "l": log,
}

#Utilities.

def is_int(token):
   return token.isdigit() or (2 <= len(token) and token[0] == "-" and token[1:].isdigit())

def is_float(token):
   tokens = token.split(".")
   return len(tokens) == 2 and is_int(tokens[0]) and tokens[1].isdigit()

#Calculator.

def rpn(stack,tok):
   #Literals.
   if is_int(tok):
      stack.append(int(tok))
   elif is_float(tok):
      stack.append(float(tok))
   
   #Binary operators.
   elif tok in binary and 2 <= len(stack):
      v2 = stack.pop()
      v1 = stack.pop()
      stack.append(binary[tok](v1,v2))
   elif tok in binary:
      sys.stderr.write("error: insufficient arguments for binary operator " + tok + "\n")

   #Unary operators.
   elif tok in unary and 1 <= len(stack):
      v = stack.pop()
      stack.append(unary[tok](v))
   elif tok in unary:
      sys.stderr.write("error: insufficient arguments for unary operator " + tok + "\n")

   #Print.
   elif tok == "p" and 1 <= len(stack):
      print stack[-1]
   elif tok == "p":
      sys.stderr.write("error: insufficient arguments to print\n")

#Input handling.

stack = []
line = sys.stdin.readline()
while 0 < len(line):
   toks = line.split()
   i = 0
   while i < len(toks):
      rpn(stack,toks[i])
      i += 1
   line = sys.stdin.readline()