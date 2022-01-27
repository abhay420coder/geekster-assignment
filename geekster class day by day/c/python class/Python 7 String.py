#                               PYTHON STRINGS

# STRINGS:- Strings in python are surrounded by 
#           either single quotation marks, or double quotation marks.

# Example :-     'hello' is the same as "hello" .











# PRINT THE  STRING :- You can display a string literal with the print() function:

# Example :-
print("Hello")
print('Hello')
print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu











# ASSIGN STRING TO A VARIABLE :- Assigning a string to a variable is done 
#                                with the variable name followed by an
#                                equal sign and the string:

# Example :-
d1 = "Hello Boy"
print(d1)
print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu
print("d1 =" , d1)
print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu











# MULTILINE STRINGS :- You can assign a multiline string to a variable by using 
#                      three quotes (three double quotes or three single quotes )

# Example :-
#               YOU CAN USE THREE DOUBLE QUOTES:-
d2 = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(d2)
print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu
print("d2 =" , d2)
print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu

#            OR YOU CAN USE THREE SINGLE QUOTES:-
d3 = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(d3)
print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu
print("d3 =" , d3)
print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu

# Note: in the result, the line breaks are inserted 
#       at the same position as in the code.














#                       STRINGS ARE ARRAYS :-

# Like many other popular programming languages, strings in Python are
# arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is
# simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

# Example:-
#           Get the character at position 1 
#           (remember that the first character has the position 0):
d4 = "Hello, World!"
print(d4[0])                  # output :- H
print(d4[1])                  # output :- e
print(d4[2])                  # output :- l
print(d4[3])                  # output :- l
print(d4[4])                  # output :- o
print(d4[5])                  # output :- ,
print(d4[6])                  # output :-  (space)
print(d4[7])                  # output :- W
print(d4[8])                  # output :- o
print(d4[9])                  # output :- r
print(d4[10])                 # output :- l
print(d4[11])                 # output :- d
print(d4[12])                 # output :- !
















#                           LOOPING THROUGH A STRING :-

# Since strings are arrays, we can loop through the characters in a string, 
#                           with a for loop.

# Example :- Loop through the letters in the word "banana":
for d5 in "banana":
 print(d5)

# Learn more about For Loops in our Python For Loops chapter.
# String Length
# To get the length of a string, use the len() function.
# Example
# The len() function returns the length of a string:
# a = "Hello, World!"
# print(len(a))
# 26/06/21, 8:55 PM
# Page 4 of 9
# Try it Yourself »
# Check String
# To check if a certain phrase or character is present in a string, we can use the
# keyword in .
# Example
# Check if "free" is present in the following text:
# txt = "The best things in life are free!"
# print("free" in txt)
# Try it Yourself »
# Use it in an if statement:
# Example
# Print only if "free" is present:
# txt = "The best things in life are free!"
# if "free" in txt:
#  print("Yes, 'free' is present.")
# Try it Yourself »
# Learn more about If statements in our Python If...Else chapter.
# 26/06/21, 8:55 PM
# Page 5 of 9
# ‹ Previous Next ›
# Check if NOT
# To check if a certain phrase or character is NOT present in a string, we can
# use the keyword not in .
# Example
# Check if "expensive" is NOT present in the following text:
# txt = "The best things in life are free!"
# print("expensive" not in txt)
# Try it Yourself »
# Use it in an if statement:
# Example
# print only if "expensive" is NOT present:
# txt = "The best things in life are free!"
# if "expensive" not in txt:
#  print("Yes, 'expensive' is NOT present.")
# Try it Yourself »
# Python - Slicing Strings
# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a
# part of the string.
# Example
# Get the characters from position 2 to position 5 (not included):
# b = "Hello, World!"
# print(b[2:5])
# Try it Yourself »
# ! " HTML CSS JAVASCRIPT SQL % $ #
# Tutorials References Menu Log in
# Paid Courses
# & ' ' '
# 26/06/21, 8:12 PM
# Page 1 of 6
# Note: The first character has index 0.
# Slice From the Start
# By leaving out the start index, the range will start at the first character:
# Example
# Get the characters from the start to position 5 (not included):
# b = "Hello, World!"
# print(b[:5])
# Try it Yourself »
# Slice To the End
# By leaving out the end index, the range will go to the end:
# Example
# Get the characters from position 2, and all the way to the end:
# b = "Hello, World!"
# print(b[2:])
# Try it Yourself »
# 26/06/21, 8:12 PM
# Page 2 of 6
# ‹ Previous Next ›
# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
# b = "Hello, World!"
# print(b[-5:-2])
# Try it Yourself 
# Python - Modify Strings
# Python has a set of built-in methods that you can use on strings.
# Upper Case
# Example
# The upper() method returns the string in upper case:
# a = "Hello, World!"
# print(a.upper())
# Try it Yourself »
# ! " HTML CSS JAVASCRIPT SQL % $ #
# Tutorials References Menu Log in
# Paid Courses
# & ' ' '
# 26/06/21, 8:56 PM
# Page 1 of 6
# Lower Case
# Example
# The lower() method returns the string in lower case:
# a = "Hello, World!"
# print(a.lower())
# Try it Yourself »
# Remove Whitespace
# Whitespace is the space before and/or after the actual text, and very often
# you want to remove this space.
# Example
# The strip() method removes any whitespace from the beginning or the
# end:
# a = " Hello, World! "
# print(a.strip()) # returns "Hello, World!"
# Try it Yourself »
# Replace String
# 26/06/21, 8:56 PM
# Page 2 of 6
# Example
# The replace() method replaces a string with another string:
# a = "Hello, World!"
# print(a.replace("H", "J"))
# Try it Yourself »
# Split String
# The split() method returns a list where the text between the specified
# separator becomes the list items.
# Example
# The split() method splits the string into substrings if it finds instances of
# the separator:
# a = "Hello, World!"
# print(a.split(",")) # returns ['Hello', ' World!']
# Try it Yourself »
# Learn more about Lists in our Python Lists chapter.
# String Methods
# Learn more about String Methods with our String Methods Reference
# Python - String Concatenation
# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
# Example
# Merge variable a with variable b into variable c :
# a = "Hello"
# b = "World"
# c = a + b
# print(c)
# Try it Yourself »
# ! " HTML CSS JAVASCRIPT SQL % $ #
# Tutorials & References & Menu Log in
# Paid Courses
# ' &
# 26/06/21, 8:56 PM
# Page 1 of 4
# ‹ Previous Next ›
# Example
# To add a space between them, add a " " :
# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)
# Try it Yourself 
# Python - Format - Strings
# String Format
# As we learned in the Python Variables chapter, we cannot combine strings
# and numbers like this:
# Example
# age = 36
# txt = "My name is John, I am " + age
# print(txt)
# Try it Yourself »
# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and
# ! " HTML CSS JAVASCRIPT SQL % $ #
# Tutorials References Menu Log in
# Paid Courses
# & ' ' '
# 26/06/21, 8:56 PM
# Page 1 of 5
# places them in the string where the placeholders {} are:
# Example
# Use the format() method to insert numbers into strings:
# age = 36
# txt = "My name is John, and I am {}"
# print(txt.format(age))
# Try it Yourself »
# The format() method takes unlimited number of arguments, and are placed
# into the respective placeholders:
# Example
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
# Try it Yourself »
# You can use index numbers {0} to be sure the arguments are placed in the
# correct placeholders:
# Example
# quantity = 3
# itemno = 567
# 26/06/21, 8:56 PM
# Page 2 of 5
# ‹ Previous Next ›
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item
# {1}."
# print(myorder.format(quantity, itemno, price))
# Try it Yourself »
# Learn more about String Formatting in our String Formatting chapter.
# Python - Escape Characters
# Escape Character
# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to
# insert.
# An example of an illegal character is a double quote inside a string that is
# surrounded by double quotes:
# Example
# You will get an error if you use double quotes inside a string that is
# surrounded by double quotes:
# txt = "We are the so-called "Vikings" from the north."
# ! " HTML CSS JAVASCRIPT SQL % $ #
# Tutorials References Menu Log in
# Paid Courses
# & ' ' '
# 26/06/21, 8:57 PM
# Page 1 of 5
# Try it »
# Try it »
# Try it »
# Try it »
# Try it »
# Try it »
# Try it »
# Try it Yourself »
# To fix this problem, use the escape character \" :
# Example
# The escape character allows you to use double quotes when you normally
# would not be allowed:
# txt = "We are the so-called \"Vikings\" from the north."
# Try it Yourself »
# Escape Characters
# Other escape characters used in Python:
# Code Result Try it
# \' Single Quote
# \\ Backslash
# \n New Line
# \r Carriage Return
# \t Tab
# \b Backspace
# \f Form Feed
# \ooo Octal value
# 26/06/21, 8:57 PM
# Page 2 of 5
# Try it »
# ‹ Previous Next ›
# \xhh Hex value
# Python - String Methods
# String Methods
# Python has a set of built-in methods that you can use on strings.
# Note: All string methods returns new values. They do not change the original
# string.
# Method Description
# capitalize() Converts the first character to upper case
# casefold() Converts string into lower case
# center() Returns a centered string
# count() Returns the number of times a specified value occurs in a
# string
# ! " HTML CSS JAVASCRIPT SQL % $ #
# Tutorials References Menu Log in
# Paid Courses
# & ' ' '
# 26/06/21, 8:57 PM
# Page 1 of 6
# encode() Returns an encoded version of the string
# endswith() Returns true if the string ends with the specified value
# expandtabs() Sets the tab size of the string
# find() Searches the string for a specified value and returns the
# position of where it was found
# format() Formats specified values in a string
# format_map() Formats specified values in a string
# index() Searches the string for a specified value and returns the
# position of where it was found
# isalnum() Returns True if all characters in the string are
# alphanumeric
# isalpha() Returns True if all characters in the string are in the
# alphabet
# isdecimal() Returns True if all characters in the string are decimals
# isdigit() Returns True if all characters in the string are digits
# isidentifier() Returns True if the string is an identifier
# islower() Returns True if all characters in the string are lower case
# isnumeric() Returns True if all characters in the string are numeric
# isprintable() Returns True if all characters in the string are printable
# isspace() Returns True if all characters in the string are whitespaces
# istitle() Returns True if the string follows the rules of a title
# isupper() Returns True if all characters in the string are upper case
# join() Joins the elements of an iterable to the end of the string
# ljust() Returns a left justified version of the string
# 26/06/21, 8:57 PM
# Page 2 of 6
# lower() Converts a string into lower case
# lstrip() Returns a left trim version of the string
# maketrans() Returns a translation table to be used in translations
# partition() Returns a tuple where the string is parted into three parts
# replace() Returns a string where a specified value is replaced with a
# specified value
# rfind() Searches the string for a specified value and returns the
# last position of where it was found
# rindex() Searches the string for a specified value and returns the
# last position of where it was found
# rjust() Returns a right justified version of the string
# rpartition() Returns a tuple where the string is parted into three parts
# rsplit() Splits the string at the specified separator, and returns a
# list
# rstrip() Returns a right trim version of the string
# split() Splits the string at the specified separator, and returns a
# list
# splitlines() Splits the string at line breaks and returns a list
# startswith() Returns true if the string starts with the specified value
# strip() Returns a trimmed version of the string
# swapcase() Swaps cases, lower case becomes upper case and vice
# versa
# title() Converts the first character of each word to upper case
# translate() Returns a translated string
# upper() Converts a string into upper case
# zfill() Fills the string with a specified number of 0 values at the
# 26/06/21, 8:57 PM
# Page 3 of 6
# ‹ Previous Next ›
# beginning
