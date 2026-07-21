"""CONTROL FLOW - pertains to the sequence of execution of statements in a program
Python incoportes various control flows statements inclduing:

with IF/ELSE: Conditional statements are utilized to execute different blocks of code depending
on whether a condition is true or false.

Loops with for and while Loops are utilized to execute a block of code repeatedly.
Python offers two types of loops: for looks and while loops.
"""
###FOR LOOPS 
print("""THE FOR LOOPS - iterate over items of a sequence and runs a code block once for each item
Sequences like strings, lists, tuples can be used with for""")

#for item in sequence:
    #code block
    
print("\n ----------------------")
print("\n")
fruits = ["apple","banana","mango"]

for fruit in fruits:
    print("I have an ",fruit)
    
print("\n ----------------------")    

##the loop VARIABLE FRUIT TAKES THE VALUE OF NEXT SEQUENCE ITEM IN EACH ITERATION
##code under loop runs 3 times, once for each item
#You can also iterate tuples, lists, dictionaryes and other sequences beside a list. 
print("\n ----------------------")

person = {"John",30,"New York"}
for value in person:
    print (value)
    
    
# to iterate  a fixed number of times instead of over a sequence, use the range () type
#range()
"""FOR i in range (start,stop, step_size)"""






