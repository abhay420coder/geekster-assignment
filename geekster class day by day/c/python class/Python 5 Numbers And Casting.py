#                               PYTHON NUMBERS :-

# There are three numeric types in Python:
# 1. int      2. float     3. complex

# Variables of numeric types are created when you assign a value to them:

# Example
b1 = 1           # int
b2 = 2.8         # float
b3 = 1j          # complex
# To verify the type of any object in Python, use the type() function:
print(type(b1))               # output :-   <class 'int'>
print(type(b2))               # output :-   <class 'float'>
print(type(b3))               # output :-   <class 'complex'>


















#                            INTEGER NUMBER (int) :-

# Int (or integer) is a whole number, 
#                       positive or negative, 
#                       without decimals, of
#                       unlimited length.

# Example
#           Integers:
b4 = 1
b5 = 35656222554887711
b6 = -3255522
print(type(b4))               # output :-   <class 'int'>
print(type(b5))               # output :-   <class 'int'>
print(type(b6))               # output :-   <class 'int'>


















#                              FLOATING POINT NUMBER (float) :-

# Float (or "floating point number") is a number, 
#                                         positive or negative, 
#                                         containing one or more decimals.

# Example
#           Floats:
b7 = 1.10
b8 = 1.0
b9 = -35.59
print(type(b7))               # output :-   <class 'float'>
print(type(b8))               # output :-   <class 'float'>
print(type(b9))               # output :-   <class 'float'>

# Float can also be scientific numbers with an "e" to indicate the power of 10.
# Example
            # Floats:
b10 = 35e3
b11 = 12E4
b12 = -87.7e100
print(type(b10))               # output :-   <class 'float'>
print(type(b11))               # output :-   <class 'float'>
print(type(b12))               # output :-   <class 'float'>



















#                   COMPLEX NUMBER (complex) :-

# Complex numbers are written with a "j" as the imaginary part:

# iska mtlb complex number ke sath "j" ka aana jaruri hai

# Example
#           complex:
b13 = 3+5j
b14 = 5j
b15 = -5j
print(type(b13))               # output :-   <class 'complex'>
print(type(b14))               # output :-   <class 'complex'>
print(type(b15))               # output :-   <class 'complex'>




















#                        TYPE CONVERSION

# You can convert from one type to another with the int() , 
#                                                   float() , 
#                                           and     complex()          methods:

# Example
#           Convert from one type to another:
b16 = 1               # int
b17 = 2.8             # float
b18 = 1j              # complex
b19 = float(b16)                    #convert from int to float:
b20 = int(b17)                      #convert from float to int:
# Note: You cannot convert complex numbers into another number type.
b21 = complex(b18)                  #convert from int to complex:
print(b19)       # output :- 1.0
print(b20)       # output :- 2
print(b21)       # output :- 1j
print(type(b19))                # output :- <class 'float'>
print(type(b20))                # output :- <class 'int'>
print(type(b21))                # output :- <class 'complex'>

# Note: You cannot convert complex numbers into another number type.



















#                           RANDOM NUMBER :-

# Python does not have a random() function to make a random number, 
# but Python has a built-in module called random 
# that can be used to make random numbers:

# Example
#          Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1, 10))                 # output :- 9
# is code ka output 1 se 9 ke beech me koi bhi number aa sakta hai

# In our Random Module Reference you will learn more about the Random module.
















#                                   PYTHON CASTING :-

# Specify a Variable Type :-

# There may be times when you want to specify a type on to a variable. 
# This can be done with casting. 

# Python is an object-orientated language, and 
# as such it uses classes to define data types, including its primitive types.

# Casting in python is therefore done using constructor functions:

# int() :-      constructs an integer number from an integer literal, 
#                                                 a float literal 
#               (by removing all decimals), 
#                                              or a string literal 
#               (providing the string represents a whole number)


# float() :-    constructs a float number from an integer literal, 
#                                              a float literal or 
#                                              a string literal 
#               (providing the string represents a float or an integer)


# str() :-      constructs a string from a wide variety of data types, 
#               including strings, integer literals and float literals


# Example
#           Integers:
b22 = int(1)           # x will be 1
b23 = int(2.8)         # y will be 2
b24 = int("3")         # z will be 3
print(b22)                 # output :- 1
print(b23)                 # output :- 2
print(b24)                 # output :- 3
#           Foats:
b25 = float(1)     # x will be 1.0
b26 = float(2.8)   # y will be 2.8
b27 = float("3")   # z will be 3.0
b28 = float("4.2") # w will be 4.2
print(b25)                 # output :- 1.0
print(b26)                 # output :- 2.8
print(b27)                 # output :- 3.0
print(b28)                 # output :- 4.2
#           Strings:
b29 = str("s1")  # x will be 's1'
b30 = str(2)     # y will be '2'
b31 = str(3.0)   # z will be '3.0'
print(b29)                 # output :- s1
print(b30)                 # output :- 2
print(b31)                 # output :- 3.0
print("b29 = " + b29)                 # output :- s1
print("b30 = " + b30)                 # output :- 2
print("b31 = " + b31)                 # output :- 3.0

