print("  ")
print("\n  ")

#arithmetic operators

a=5
b=10
c=5.5
z = a + b #addition
print(z)
Z=a-b #subtraction
print(Z)
Z=a*b #Multiplication
print(Z)
Z=a/b #division
print(z)
Z=a%b #Modulo remaider
print(z)
Z=a**b #Exponent
print(z)
Z=a//b #Integer Division
print(z)

Z=c//b #Integer Division
print(z)
z=c/a #division
print(z)

print("\n  ")
print("  ")
#Comparison Operators
x=3
y=2
print(x==y) #equal
print(x!=y) #not equal
print(x>y)  #greater than
print(x<y)  #less than
print(x>=y) #greater than or equal to
print(x<=y) #less than or equal to

print("\n  ")
#Logical Operators
a=True
b=False
print(a and b) #and operator
print(a or b)  #or operator
print(not a)   #not operator

print("\n  ")
#Bitwise Operators
x=2  #binary 10
y=3  #binary 11
print(x & y) #AND operator, binary 10 which is 2 in decimal
print(x | y) #OR operator, binary 11 which is 3 in decimal
print(x ^ y) #XOR operator, binary 01 which is 1 in decimal
print(~x)    #NOT operator, binary -11 which is -3 in decimal
print(x << 1) #Left shift operator, binary 100 which is 4 in decimal
print(x >> 1) #Right shift operator, binary 01 which is 1 in decimal

print("\n  ")
#Experiment with integer vs. float division using the / and // operators to see the difference in behavior.
print("\n  ")
# Integer division (both operands integers)

print(10 / 2)   # 5.0 (evenly divisible, but still float)
print(10 / 3)   # 3.3333333333333335 (approximate float result)

print("\n  ")
# Float division (at least one operand float)
print(10.0 / 2) # 5.0
print(10 / 3.0) # 3.3333333333333335

print("\n  ")
# Both floats
print(10.0 / 2.5) # 4.0

print("\n  ")
# Integer floor division (both operands integers)
print(10 // 3)    # 3 (integer result)
print(-10 // 3)   # -4 (rounds down to next integer)

print("\n  ")
# Mixed float floor division
print(10.0 // 3)  # 3.0 (float result, but floored)
print(10 // 3.0)  # 3.0
print(-10 // 3.0) # -4.0

print("\n  ")
# Both floats
print(10.0 // 2.5) # 4.0 (since 2.5*4=10)
print(11.5 // 2.5) # 4.0 (2.5*4=10, remainder 1.5)

print("\n  ")
#Excercise use the % modulo operator applied to integers and observe the remainder result

print("\n  ")
#using positive numbers
print(10 % 3)    # 1 (10 ÷ 3 = 3 with remainder 1)
print(15 % 4)    # 3 (15 ÷ 4 = 3 with remainder 3)
print(20 % 5)    # 0 (20 ÷ 5 = 4 exactly, no remainder)
print(7 % 10)    # 7 (7 ÷ 10 = 0 with remainder 7)

print("\n  ")
#using modulo with negative numbers
print(-10 % 3)   # 2 (This might surprise you!)
print(10 % -3)   # -2 (Different from above!)
print(-10 % -3)  # -1 (Same sign as divisor)

print("\n  ")
#common use case for % modulo operator 
print("\n  ")
#check if number is even or odd

print(15 % 2)# 1 (odd)
print(16 % 2) # 0 (even)
#Get Last digit of a number
print(253 % 10) # 3
print(1984 % 10)# 4
#Circular Wrapping (great for games, clocks..)
print(15 % 12) # 3 o clock
print (25 % 24)# 1am next day
#edge cases 
print(0 % 5 ) # 0 (0 ÷ anything has remainder 0)
print (5 % 1) # 0 (any number ÷ 1 has remainder 0)
print (5 %0) # ZeroDivisionError (can't divide by zero)


print("""\n Key Observations:With positive numbers, behaves as expected (returns remainder)

With negative numbers, result takes sign of the divisor (second operand)

Always returns zero when dividend is multiple of divisor

Very useful for cyclic patterns and digit extraction """)