print("\n  ")
print("  ")
#Exercise 1 -experiment with comparison operatos using different integer, float and string variables to observe boolean outcomes.

print("\n  ")#1. Numeric Comparisons (Integers & Floats)
print("\n  ")# Equality (==) and Inequality (!=)
print (5==5) #True (int ==int)
print (5==5.0) #True (int == float, value matches)
print(5.0 == 5.0)   #True (float == float)
print (5!=3) # True (5 is not equal to 3)

print("\n  ")#Greater/ Less than
print(10>5) #True
print(3.5<3) #false
print(4.0 >= 4) # True (float 4.0 is equal to int 4)
print(2<= 2.0) # True (2 is equal to 2.0)

print("\n  ")#2. String Comparisons (Lexicographical Order)
print("\n  ")# Equality (==) and Inequality (!=)
print("hello" == "hello")  # True (identical strings)
print("Hello" == "hello")  # False (case-sensitive)
print("abc" != "def")      # True (different strings)

print("\n  ")# Greater/Less than (lexicographical order)
print("apple" < "banana")  # True ('a' comes before 'b')
print("cat" > "dog")       # False ('c' < 'd')
print("Zebra"<"apple") # True (uppercase 'Z' < lowercase 'a' in Unicode)

print("\n  ")# Comparing strings of different lengths
print("hi"<"hello")  # False ('i' (105) > 'e' (101))
print("Python" >= "Java")  # True ('P' (80) > 'J' (74))

print("\n  ")#3. Mixed-Type Comparisons (Numbers vs. Strings)
print("\n  ")# Numbers and strings are NEVER equal
print(5 == "5")        # False (int vs. string)
print(3.0 == "3.0")    # False (float vs. string)

print("\n  ")# Comparing incompatible types with > or < raises TypeError
#print(10 > "5")        # TypeError: '>' not supported between 'int' and 'str'
#print("10" < 5)        # TypeError: '<' not supported between 'str' and 'int'

print("\n  ")#4. Chained Comparisons
print("\n  ")# Numeric chaining
print(5 < 10 <= 15)        # True (5 < 10 AND 10 <= 15)
print(3.5 == 3.5 < 4.0)    # True (3.5 == 3.5 AND 3.5 < 4.0)

print("\n  ")# String chaining
print("a" < "b" < "c")     # True (lexicographical order)
print("A" < "a" < "z")     # True ('A' < 'a' < 'z' in Unicode)

print("\n  ")#5. Special Cases
print("\n  ")# Comparing booleans (True=1, False=0)
print(True == 1)       # True (bool is a subclass of int)
print(False < 1)       # True (0 < 1)
print(True == "True")  # False (bool vs. string)

print("\n  ")# None only equals None
print(None == None)    # True
print(None == 0)       # False

print("\n  ")#Excercise 2 Try building compound logical boolean expresions with AND, OR, NOT operators.
print("\n  ")# Exploring Compound Boolean Expressions with AND, OR, NOT
print("\n  ")#Let's experiment with combining comparison operators using logical operators (and, or, not) to create more complex conditions.

print("\n  ")#1.Basic Logical Operations

print("\n  ")#1. AND Operator (Both conditions must be True)
print("\n  ")#1 Numeric examples
print(not 5 > 3)              # False (5 > 3 is True, inverted)
print(not 10 == 20)           # True (10 == 20 is False, inverted)

print("\n  ")#2 String examples
print(not "a" == "A")         # True (strings unequal, inverted False)
print(not "python".startswith("p")) # False (True condition inverted)
#Combining Multiple Logical Operators

print("\n  ")#2. Mixed AND/OR with Parentheses
print("\n  ")#1 Without parentheses (order of operations: not > and > or)
print(True or False and False)  # True (and evaluated first)
print((True or False) and False) # False (parentheses change order)

print("\n  ")#2 More complex example
age = 25
name = "Alice"
print(age > 18 and (name == "Alice" or name == "Bob"))  # True

print("\n  ")#5. Real-world Examples
print("\n  ")# Password checker
password = "Secure123"
print(len(password) >= 8 and any(c.isupper() for c in password))  # True

print("\n  ")# Temperature range
temp = 22.5
print(temp >= 20 and temp <= 25)  # Comfortable room temperature

print("\n  ")# Username validation
username = "user_123"
print(len(username) >= 5 and "_" in username and not username.startswith("admin"))  # True

print(""" Truth Table Examples
Let's examine how Python evaluates truthiness:

Expression	    Evaluation	       Result
True and True	Both True	True
True and False	Second False	False
False or True	Second True	True
not False	    Inverts False	True
0 and 5	0 is falsy	0
"" or "hello"	Empty string is falsy	"hello"
 """)

print("\n  ")#Short-circuit Evaluation
print("\n  ")#OR stops at first True
print("\n  ")#Python stops evaluating as soon as the result is determined:
print(True or(1/0)) #True (never evaluates division by zero)
#and stops at first False
print(False and (1/0)) # False (avoids division by zero)

print("\n  ")#Practical Applications
print("\n  ")#Validating user input
age = 30
has_license = True
print(age >= 18 and has_license) #Can Drive

print("\n  ")#Discount eligibility 
is_member = True
purchase_amount = 120
print(is_member or purchase_amount > 100) #Eligible for discount

print("\n  ")#Complex condition
temperature = 28
is_summer = True
print((temperature > 25 and is_summer) or (temperature > 20 and not is_summer)) #True

print("\n  ")#Excercise 3 -look up bitwise operators documentation and test out their functionality on sample integer values to learn.
print("\n  ")#Exploring Python Bitwise Operators
#1. Bitwise AND (&)
#perform a logical AND on each bit pair
# 5 = 0101, 3 = 0011
print(5 & 3)  # 0101 & 0011 = 0001 (1)
# 12 = 1100, 7 = 0111
print(12 & 7) # 1100 & 0111 = 0100 (4)
#2. Bitwise OR (|)
#Performs a logical OR on each bit pair.
# 5 = 0101, 3 = 0011
print(5 | 3)  # 0101 | 0011 = 0111 (7)
# 12 = 1100, 7 = 0111
print(12 | 7) # 1100 | 0111 = 1111 (15)
#3. Bitwise XOR (^)
#Performs an exclusive OR (1 if bits differ, 0 if same).
# 5 = 0101, 3 = 0011
print(5 ^ 3)  # 0101 ^ 0011 = 0110 (6)
# 12 = 1100, 7 = 0111
print(12 ^ 7) # 1100 ^ 0111 = 1011 (11)

#4. Bitwise NOT (~) 
#Flips all bits (including sign bit - results in negative numbers).
# 5 = 00000101 → ~5 = 11111010 (two's complement)
print(~5)  # -6
print(~-3) # 2 (because -3 = 11111101 → ~-3 = 00000010)

#5. Left Shift (<<)
#Shifts bits left, filling with 0s. Equivalent to multiplying by 2ⁿ.
# 5 = 0101
print(5 << 1)  # 1010 (10)
print(5 << 2)  # 10100 (20)
print(3 << 3)  # 3*2³ = 24

#6. Right Shift (>>)
#Shifts bits right, preserving sign. Equivalent to integer division by 2ⁿ.
# 10 = 1010
print(10 >> 1)  # 0101 (5)
print(10 >> 2)  # 0010 (2)
print(-8 >> 1)  # -4 (preserves sign)   

#Practical Applications
#1. Checking Even/Odd
num = 7
if num & 1:
    print("Odd")  # 0111 & 0001 = 0001 (True)
else:
    print("Even")

#2. Swapping Variables
a, b = 5, 9
a ^= b
b ^= a
a ^= b
print(a, b)  # 9, 5

#3. Flags/Permissions
READ = 0b0001
WRITE = 0b0010
EXECUTE = 0b0100

permissions = READ | WRITE  # 0011
print(bin(permissions))  # '0b11'

if permissions & READ:
    print("Read allowed")
    
#4. Fast Multiplication/Division    

print(16 << 1)  # 32 (16*2)
print(16 >> 1)  # 8 (16/2)
print(7 << 3)   # 56 (7*8)

#NEGAVTIVE NUMBER HANDLING
#Python uses two's complement for negative numbers: 

print(bin(-5 & 0xff))  # Shows 8-bit representation: '0b11111011'
print(-5 >> 1)         # -3 (not -2, because sign is preserved)
