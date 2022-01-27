# VARIABLE DECLARATION :-

# Python has no Command for declaring a variable

# variable ko declare krne ke liye python
# ke paas koi command nhi hai

# A variable is created the moment you first assign a value to it.  

e1=5
e2=4
print (e1)                    # output :-  5
print (e2)                    #            4

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu



# Variables do not need to be declared with any particular type, and can even
# change type after they have been set.

# Example
e3 = 4                   # e3 is of type int
e3 = "Mally"             # e3 is now of type str
print(e3)                # output :-   Mally

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu












# String variables can be declared either by using single quotes ('') or 
# double quotes (" ")

# string variable ko yaa to single quotes yaa double quotes se declare kr sakte hai

#example
e4="sallu"
e5='goes to home'
print (e4)                    # output :-   sallu
print (e5)                    #             goes to home

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu
















# RULES FOR PYTHON VARIABLE NAMES :-

# A variable can have a short name (like x and y) or a more descriptive name
# (age, carname, total_volume). Rules for Python variables:

#  1:->  A variable name must start with a letter or the underscore character
#  2:->  A variable name cannot start with a number
#  3:->  A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#  4:->  Variable names are case-sensitive 
#        (age, Age and AGE are three different variables)

# LEGAL VARIABLE NAMES:-
myvar = "John1"              
my_var = "John2"             
_my_var = "John3"            
myVar = "John4"              
MYVAR = "John5"              
myvar2 = "John6"           

print (myvar)               # output :-   John1
print (my_var)              #             John2
print (_my_var)             #             John3
print (myVar)               #             John4
print (MYVAR)               #             John5
print (myvar2)              #             John6

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu


# ILLEGAL VARIABLE NAMES:-
#  2myvar = "John"
#  my-var = "John"
#  my var = "John"

















# SEVERAL TECHNIQUES YOU CAN USE TO MAKE VARIABLE MORE READABLE:-
# 1. Camel Case      2. Pascal Case      3. Snake Case 

# CAMEL CASE :- Each word, except the first, starts with a capital letter:
myVariableName = "John7"
print (myVariableName)               # output :-   John7

# PASCAL CASE :- Each word starts with a capital letter:
MyVariableName = "John8"
print (MyVariableName)               # output :-   John8

# SNAKE CASE :- Each word is separated by an underscore character:
my_variable_name = "John9"
print (my_variable_name)             # output :-   John9

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu

















# CASE SENSITIVE :- Variable names are case-sensitive.

# Example
e6 = 4
E6 = "Sally"           # E will not overwrite e
print (e6)             # output :-   4
print (E6)             # output :-   Sally

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu













# CASTING :- If you want to specify the data type of a variable, 
#            this can be done with casting

# Example :-
e7 = str(3)             # x will be '3'
e8 = int(3)             # y will be 3
e9 = float(3)           # z will be 3.0
print (e7)              # output :-   3
print (e8)              # output :-   3
print (e9)              # output :-   3.0

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu














# GET THE TYPE :- You can get the data type of a variable with the type() function

# Example
e10 = 5
e11 = "John"
print(type(e10))              # output :-   <class 'int'>
print(type(e11))              # output :-   <class 'str'>

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu














# MANY VALUES TO MULTIPLE VARIABLES :- Python allows you to assign values to 
#                                      multiple variables in one line:

# Example
e12, e13, e14 = "Orange", "Banana", "Cherry"
print(e12)               # output :-   Orange
print(e13)               #             Banana
print(e14)               #             Cherry

# NOTE :- Make sure the number of variables matches the number of values, or
#         else you will get an error.

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu













# ONE VALUE TO MULTIPLE VARIABLES :- And you can assign the same value to
#                                     multiple variables in one line:

# Example
e15 = e16 = e17 = "Orange"
print(e15)               # output :-   Orange
print(e16)               #             Orange
print(e17)               #             Orange

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu












# UNPACK A COLLECTION :- If you have a collection of values in a list, tuple etc. 
#                        Python allows you extract the values into variables. 
#                        This is called unpacking.

# Example :- Unpack a list:
fruits = ["apple", "banana", "cherry"]
e18, e19, e20 = fruits
print(e18)               # output :-   apple
print(e19)               #             banana
print(e20)               #             cherry

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu














# OUTPUT VARIABLES :- The Python print statement is often used to output variables.
#                     To combine both text and a variable, Python uses the + character:

# Example
e21 = "wow-wow"
print("Python is " + e21)               # output :-   Python is wow-wow

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu

#  You can also use the + character to add a variable to another variable 
#  in same data type :

# Example
e22 = "Python is "
e23 = "awesome"
e24 = e22 + e23
print(e24)               # output :-   Python is awesome

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu


# NOTE :-   For numbers, the + character works as a mathematical operator

# Example
e25 = 5
e26 = 10
print(e25 + e26)               # output :-   15

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu



# NOTE :-  If you try to combine a string and a number, Python will give you an error:

# Code:-       x = 5
#              y = "John"
#              print(x + y)      // is code ka output error hoga    

















# GLOBAL VARIABLES:- Variables that are created outside of a function 
#                     (as in all of the examples above) are known as global variables.

#                     Global variables can be used by everyone, 
#                     both inside of functions and outside.

# Example
#          Create a variable outside of a function, and use it inside the function

e27 = "best"

def myfunc1():
  print("Python is " + e27)

myfunc1()                      # output :-   Python is best

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu


# NOTE :-  If you create a variable with the same name inside a function, 
#          this variable will be local, and can only be used inside the function. 

#          The global variable with the same name will remain as it was, 
#          global and with the original value.


# Example
#           Create a variable inside a function, with the same name as the global variable

e28 = "outstanding"

def myfunc2():
    e28 = "enjoyed"
    print("Python is " + e28)

myfunc2()                              # output :-   Python is enjoyed

print("Python is " + e28)               # output :-   Python is outstanding

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu















# THE GLOBAL KEYWORD :- Normally, when you create a variable inside a function, 
#                       that variable is local, and can only be used inside that function.

#                       To create a global variable inside a function, 
#                       you can use the global keyword.


# Example
#            If you use the global keyword, the variable belongs to the global scope:

def myfunc():
   global e29
   e29 = "good"

myfunc()

print("Python is " + e29)               # output :-   Python is good

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu



# NOTE :- Also, use the global keyword if you want to change a global variable inside
#         a function.


# Example
#          To change the value of a global variable inside a function, 
#          refer to the variable by using the global keyword:

e30 = "chily"

def myfunc():
   global e30
   e30 = "lily"

myfunc()

print("Python is " + e30)               # output :-   Python is lily
