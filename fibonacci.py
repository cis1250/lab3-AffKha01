#!/usr/bin/env python3

# Fibonacci Sequence Exercise
# TODO: (Read detailed instructions in the Readme file)
# Prompt the user for the number of terms.
# Validate that the input is a positive integer.
# Use a for loop to print the Fibonacci sequence up to that many terms.
while (true):
  terms = input("Please enter the number of terms")
  if (terms <= 0):
    print("Incorrect input, please input a integer greater than 0")
  else:
    break;

def fibonacci (terms):
  if (terms == 1):
    return 0
  else if (terms == 2):
    return 1
  else:
    return fibonacci(terms - 1) + fibonacci (terms - 2)

for i in range (terms):
  print(fibonacci(i), end= " ")
  
  
