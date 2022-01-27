
# BUILT-IN DATA TYPES :- 

# In programming, data type is an important concept.

# Variables can store data of different types, 
# and different types can do different things.

# Python has the following data types built-in by default, in these categories:

#  Text Type        :-       str
#  Numeric Types    :-       int   ,    float       , complex
#  Sequence Types   :-       list  ,    tuple       , range
#  Mapping Type     :-       dict
#  Set Types        :-       set   ,    frozenset
#  Boolean Type     :-       bool
#  Binary Types     :-       bytes ,    bytearray   , memoryview














# GETTING THE DATA TYPE :-  
#        You can get the data type of any object by using the type() function:

# Example :-
#            Print the data type of the variable x:
a1 = 5
print(type(a1))               # output :-   <class 'int'>

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu























# SETTING THE DATA TYPE :- In Python, the data type is set when you assign a value to a variable:

#   no.       Example                                           Data Type 
#   1.        x = "Hello World"                                    str
#   2.        x = 20                                               int
#   3.        x = 20.5                                             float
#   4.        x = 1j                                               complex
#   5.        x = ["apple", "banana", "cherry"]                    list
#   6.        x = ("apple", "banana", "cherry")                    tuple
#   7.        x = range(6)                                         range
#   8.        x = {"name" : "John", "age" : 36}                    dict
#   9.        x = {"apple", "banana", "cherry"}                    set
#   10.       x = frozenset({"apple", "banana", "cherry"})         frozenset
#   11.       x = True                                             bool
#   12.       x = b"Hello"                                         bytes
#   13.       x = bytearray(5)                                     bytearray
#   14.       x = memoryview(bytes(5))                             memoryview


a2 = "Hello World"
# display a2 :-
print (a2)                                # output :-   Hello World
# display the data type of a2 :-
print (type(a2))                          # output :-   <class 'str'>

a3 = 20  
# display a3 :-
print (a3)                                # output :-   20
# display the data type of a3 :-
print (type(a3))                          # output :-   <class 'int'>

a4 = 20.5 
# display a4 :-
print (a4)                                # output :-   20.5
# display the data type of a4 :-
print (type(a4))                          # output :-   <class 'float'>

a5 = 1j  
# display a5 :-
print (a5)                                # output :-   1j
# display the data type of a5 :-
print (type(a5))                          # output :-   <class 'complex'>

a6 = ["apple", "banana", "cherry"] 
# display a6 :-
print (a6)                                # output :-   ['apple', 'banana', 'cherry']
# display the data type of a6 :-
print (type(a6))                          # output :-   <class 'list'>

a7 = ("apple", "banana", "cherry")  
# display a7 :-
print (a7)                                # output :-   ('apple', 'banana', 'cherry')
# display the data type of a7 :-
print (type(a7))                          # output :-   <class 'tuple'>

a8 = range(6)   
# display a8 :-
print (a8)                                # output :-   range(0, 6)
# display the data type of a8 :-
print (type(a8))                          # output :-   <class 'range'>

a9 = {"name" : "John", "age" : 36}  
# display a9 :-
print (a9)                                # output :-   {'name': 'John', 'age': 36}
# display the data type of a9 :-
print (type(a9))                          # output :-   <class 'dict'>

a10 = {"apple", "banana", "cherry"} 
# display a10 :-
print (a10)                                # output :-   {'apple', 'banana', 'cherry'}
# display the data type of a10 :-
print (type(a10))                          # output :-   <class 'set'>

a11 = frozenset({"apple", "banana", "cherry"})    
# display a11 :-
print (a11)                                # output :-   frozenset({'apple', 'banana', 'cherry'})
# display the data type of a11 :-
print (type(a11))                          # output :-   <class 'frozenset'>

a12 = True  
# display a12 :-
print (a12)                                # output :-   True
# display the data type of a12 :-
print (type(a12))                          # output :-   <class 'bool'>

a13 = b"Hello"   
# display a13 :-
print (a13)                                # output :-   b'Hello'
# display the data type of a13 :-
print (type(a13))                          # output :-   <class 'bytes'>

a14 = bytearray(5) 
# display a14 :-
print (a14)                                # output :-   bytearray(b'\x00\x00\x00\x00\x00')
# display the data type of a14 :-
print (type(a14))                          # output :-   <class 'bytearray'>

a15 = memoryview(bytes(5))
# display a15 :-
print (a15)                                # output :-   <memory at 0x000001FDFC953C40>
# display the data type of a15 :-
print (type(a15))                          # output :-   <class 'memoryview'>

print("\n")        #  mai ia code ka use output me ek line gap lane ke liye kr rha hu





















# SETTING THE SPECIFIC DATA TYPE :- If you want to specify the data type, 
#                                   you can use the following constructor functions:

#   no.       Example                                                 Data Type 
#   1.        x = str("Hello World")                                    str
#   2.        x = int(20)                                               int
#   3.        x = float(20.5)                                           float
#   4.        x = complex(1j)                                           complex
#   5.        x = list(("apple", "banana", "cherry"))                   list
#   6.        x = tuple(("apple", "banana", "cherry"))                  tuple
#   7.        x = range(6)                                              range
#   8.        x = dict(name="John", "age"=36)                           dict
#   9.        x = set(("apple", "banana", "cherry"))                    set
#   10.       x = frozenset(("apple", "banana", "cherry"))              frozenset
#   11.       x = bool(5)                                               bool
#   12.       x = bytes(5)                                              bytes
#   13.       x = bytearray(5)                                          bytearray
#   14.       x = memoryview(bytes(5))                                  memoryview


a16 = str("Hello World")
# display a16 :-
print (a16)                                # output :-   Hello World
# display the data type of a16 :-
print (type(a16))                          # output :-   <class 'str'>

a17 = int(20)  
# display a17 :-
print (a17)                                # output :-   20
# display the data type of a17 :-
print (type(a17))                          # output :-   <class 'int'>

a18 = float(20.5)
# display a18 :-
print (a18)                                # output :-   20.5
# display the data type of a18 :-
print (type(a18))                          # output :-   <class 'float'>

a19 = complex(1j) 
# display a19 :-
print (a19)                                # output :-   1j
# display the data type of a19 :-
print (type(a19))                          # output :-   <class 'complex'>

a20 = list(("apple", "banana", "cherry")) 
# display a20 :-
print (a20)                                # output :-   ['apple', 'banana', 'cherry']
# display the data type of a20 :-
print (type(a20))                          # output :-   <class 'list'>

a21 = tuple(("apple", "banana", "cherry"))   
# display a21 :-
print (a21)                                # output :-   ('apple', 'banana', 'cherry')
# display the data type of a21 :-
print (type(a21))                          # output :-   <class 'tuple'>

a22 = range(6)   
# display a22 :-
print (a22)                                # output :-   range(0, 6)
# display the data type of a22 :-
print (type(a22))                          # output :-   <class 'range'>

a23 = dict(name="John", age=36) 
# display a23 :-
print (a23)                                # output :-   {'name': 'John', 'age': 36}
# display the data type of a23 :-
print (type(a23))                          # output :-   <class 'dict'>

a24 = set(("apple", "banana", "cherry"))   
# display a24 :-
print (a24)                                # output :-   {'apple', 'banana', 'cherry'}
# display the data type of a24 :-
print (type(a24))                          # output :-   <class 'set'>

a25 = frozenset(("apple", "banana", "cherry"))    
# display a11 :-
print (a25)                                # output :-   frozenset({'apple', 'banana', 'cherry'})
# display the data type of a11 :-
print (type(a25))                          # output :-   <class 'frozenset'>

a26 = bool(5) 
# display a26 :-
print (a26)                                # output :-   True
# display the data type of a26 :-
print (type(a26))                          # output :-   <class 'bool'>

a27 = bytes(5)  
# display a27 :-
print (a27)                                # output :-   b'\x00\x00\x00\x00\x00'
# display the data type of a27 :-
print (type(a27))                          # output :-   <class 'bytes'>

a28 = bytearray(5) 
# display a28 :-
print (a28)                                # output :-   bytearray(b'\x00\x00\x00\x00\x00')
# display the data type of a28 :-
print (type(a28))                          # output :-   <class 'bytearray'>

a29 = memoryview(bytes(5))
# display a29 :-
print (a29)                                # output :-   <memory at 0x0000027AE0D93B80>
# display the data type of a29 :-
print (type(a29))                          # output :-   <class 'memoryview'>