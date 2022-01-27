# Add Two Numbers
c1 = 7.8
c2 = 6.5
c3 = c1 + c2
print ( "c1 = " , c1  )
print ( "c2 = " , c2  )
print ( "c3 = " , c3  )

# Add Two Numbers
c4 = 9.8
c5 = 12.7
c6 = c1 + c2
print ( "c4 = " , c4 , "c5 = " , c5 , "c6 = " , c6   )

# Add Two Numbers
c7 = 22.9
c8 = 24.7
c9 = c7 + c8
print ( "The Sum Of {0} and {1} is {2}" .format( c7, c8, c9))
# niche line se app format ko use krne ka pattern dekhe ...... isi ke liye niche wala line likhe hai
print ( "The Sum Of {0} and {1} is {2} aur {3} and {4} ka zor {5} hai" .format( c7, c8, c9 , c7 , c8 ,c9))
# overall format ke use krne  ka pattern ye hai

# print ( "sentence {0} sentence {1} sentence {2} sentence {3} sentence {4}.......sentence {n}" .format( Var0, Var1, Var2, Var3, Var4, ...... Varn))

# "\n"is used for new line


# Add Two Numbers
c10 = 3.2
c11 = 7.3
c12 = c10 + c11
print ( "c10 = " , c10 , "\n" , "c11 = " , c11 , "\n" , "c12 = " , c12   )

















# Add Two Number With User Input
c13 = input("enter first number = ")
c14 = input("enter Second number = ")
c15 = float(c13) + float(c14)
print ( "c13 = " , c13 , "\n" , "c14 = " , c14 , "\n" , "c15 = " , c15   )

print ( "The Sum Of {0} and {1} is {2}" .format( c13, c14, c15))



# Add Two Number With User Input In Single Line
print("the sum is %1f " %(float(input("enter 1st number : ")) + float(input("enter 2nd number : "))))

# Add Two Number With User Input In Single Line
print(   "the sum is %1f " 
          %(float(input("enter 1st number : ")) 
                +
           float(input("enter 2nd number : "))))
