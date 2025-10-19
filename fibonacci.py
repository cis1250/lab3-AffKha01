#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
while (True):
  print("Please enter the number of terms")
  terms = int(input())
  if (terms <= 0):
    print("Incorrect input, please input a integer greater than 0")
  else:
    break

def fibonacci (terms):
  if (terms == 0):
    return 0
  if (terms == 1):
    return 0
  elif (terms == 2):
    return 1
  else:
    return fibonacci(terms - 1) + fibonacci (terms - 2)

for i in range (1, terms + 1):
  print(fibonacci(i), end= " ")
  
print("")
  
  
# your code breaks with a string input. -1
