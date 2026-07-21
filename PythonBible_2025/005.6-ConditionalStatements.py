print("\n  ")
print(" ")

#PYTHON CONDITIONAL STATEMENTS
print("PYTHON CONDITIONAL STATEMENTS")
"""PYTHON provides thre main conditional statements to control the flow of execution - if, else and elif statements. These allow checking conditions  and executing different blocks of code based on whether the conditions evaluate to True or False. Conditional Statements are extremely useful in writing Python programs that can make decisions. Let's lear about each of these in detail"""

#IF STATEMENTS
print("\n --IF STATEMENTS--\n The if statement is used to check a condition and execute a block of code if there condition evaluate to True. The basic sintax is: ")
num = 15
if num > 10:
    print ("\n Num is greater than 10")

#IF ELSE STATEMENT
print("\n IF-ELSE STATEMENT \n\n The if-else statement allows executing one block of code if the condition is True and another block of code if the conditino si False. \n The syntax is: ")    
num = 7

if num > 10:
    print("\n Num is greater than 10")
else:
    print("\n Num is less than 10")
    
#The else block Allows covering both cases with if and else blocks- when the condition is True or False.

#ELIF Statement

print("\n -ELIF STATEMENT- \n The elif statement allows chaining multiple conditions to check and executing different code blocks on the first condition that evaluates to True. \n For example:")
num = 15
if num>20:
    print("\n Num is greater than 20")
elif num >10:
    print("NUm is greater than 10")
elif num >5:
    print("Num is greater than 5")
else:
    print("Num is less than 5 ")

print("\n NESTED IF STATEMENT \n --Conditional statements can also be nested to check complex conditions with multiple decissions possible. Nested if statements have an if condition inside another if or else block.\n for example: \n ")

num =14
if num>=10:
    print("Num is greater than 10")
    if num ==14:
        print("Specifically num is 14")
    
print("\n First the outer num>= is donde which is true here. So the nested if block is reached an here num ==14 so again prints. \n Specifically num is 14 nesting conditional statements controls execution flow across multiple checks and conditional codes")

#ONE LINE CONDITIONAL STATEMENTS

print("\n ONE LINE CONDITIONAL STATEMENTS \n Small conditional checks can be written in a single line for brevity using ternary operators and lambdas as given below:  ")

value = 10 if num > 5 else 0 # ternary operators
is_positive = (lambda num: True if num >0 else False) (value) #Lambda function

print("\n Here for the ternary operator, if num >5 to True, value is set to 10, else it is set to 0. Similarly, the lambda function checks if value is >0")

#MULTIPLE CONDITIONS IN IF STATEMENTS
print("\n MULTIPLE CONDITIONS IN IF STATEMENT \n an If statement can also check multiple conditions using logical operators like and or For example:")

num = 15
if num >= 10 and num <= 20: 
    print("Between 10 and 20")

print("\n This checks two conditions joined with a logical and operator. Both conditins need to evaluate to True for the overall condition to be True and the code inside the if to execute \n Similarly or can be used tockec if any one of multiple conditions is True. Multiple complex conditions can be built using logical operators in this way")

#EXCERCISES

"""
1. Write an IF-ELSE statement that prints -num is odd- if the num variable holds on odd number and -num- is even- if it holds an even number
2. Write an If-elif-else Chain that prints -POSITIVE- if num>0 -Negative- if num < 0 and Zero if num = 0 
3. Write nested if statements for the following logic- if age>60, print -Senior citizen-. If age is also >=65, print -additional benefits eligible. 
4.Convert the nested if statement in 3. to use only if-elif-else-statements
5.Write a one line conditional statement using lambda to check if num is divisible by 5
6. Write an if statement that prints -Valid- if var starts with A or B or C is 10 to20 characters long else print -Invalid-
"""





    
    


