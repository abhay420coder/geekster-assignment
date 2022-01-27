# Python Lambda
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only
# have one expression.
# Syntax
# lambda arguments : expression
# The expression is executed and the result is returned:
# Example
# Add 10 to argument a , and return the result:
# x = lambda a : a + 10
# print(x(5))
# ! " HTML CSS JAVASCRIPT SQL % $ #
# Tutorials References Menu Log in
# Paid Courses
# & ' ' '
# 26/06/21, 9:24 PM
# Page 1 of 8
# Try it Yourself »
# Lambda functions can take any number of arguments:
# Example
# Multiply argument a with argument b and return the result:
# x = lambda a, b : a * b
# print(x(5, 6))
# Try it Yourself »
# Example
# Summarize argument a , b , and c and return the result:
# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))
# Try it Yourself »
# 26/06/21, 9:24 PM
# Page 2 of 8
# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous
# function inside another function.
# Say you have a function definition that takes one argument, and that
# argument will be multiplied with an unknown number:
# def myfunc(n):
#  return lambda a : a * n
# Use that function definition to make a function that always doubles the
# number you send in:
# Example
# def myfunc(n):
#  return lambda a : a * n
# mydoubler = myfunc(2)
# print(mydoubler(11))
# Windows Can Run on Mac
# Windows on Mac. macOS Catalina/Big Sur+Windows 10 Optimized. Mac Features
# in Windows. Try! parallels.com
# Download
# 26/06/21, 9:24 PM
# Page 3 of 8
# Try it Yourself »
# Or, use the same function definition to make a function that always triples
# the number you send in:
# Example
# def myfunc(n):
#  return lambda a : a * n
# mytripler = myfunc(3)
# print(mytripler(11))
# Try it Yourself »
# Or, use the same function definition to make both functions, in the same
# program:
# Example
# def myfunc(n):
#  return lambda a : a * n
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(11))
# print(mytripler(11))
# Try it Yourself »
# 26/06/21, 9:24 PM
# Page 4 of 8
# ‹ Previous Next ›
# Use lambda functions when an anonymous function is required for a short
# period of time.
# Test Yourself With Exercises

