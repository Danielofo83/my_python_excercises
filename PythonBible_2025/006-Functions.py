""""FUNCTIONS AND PARAMETERS """
print("FUNCTIONS AND PARAMETERS")


def greet(name):
    print(f"Hello,{name}!")

greet("Luis")
greet("Alicia")
greet("Joel")

print("\n POSITIONAL AND KEYWORD ARGUMENTS -- functions can take in parameters in two ways: Positional and keyword arguments are passed in order while keywords areguments are passed using the argument name. Here's an example ")



def describe_pet(name,animal_type):
    print(f"My {animal_type}'s name is {name}.")    

print("\n in this call is passed as the first argument and second argument")
describe_pet("Mika","dog")

print("\n in this second call the order is reversed,but the argument names are explicitly stated. Both calls to the function will aoutput below")

describe_pet(animal_type="cat",name="whiskers")

#USER DEFINED VS BUILT IN FUNCTIONS
"""Notes to be added here
def function_name (parameters):
statements
return value
"""
print("\n let's see an example of the fuction definition")

def add_nums(num1,num2):
    sum= num1 + num2
    return sum
#simplificado
print(add_nums(1,2))
#mas largo.
result=add_nums(5,5)
print(result)

print(len("palabra"))
print(int("3"))
print(float("4.5555"))


maximo=30.5555555
print(f"el valor Maximo por el momento como float es el siguiente {maximo}")
print(f"el valor establecido es el siguiente por metodo round {round(maximo)}")


""" 
1. Define a function calculate_sum() that takes in a numeric list as argument and returns the sum of all numbers in that list. Call this function to find the sum of list[10,15,20] and print it. 
2. Print the absolute value of -15 using the built-in abs() function. Also print the minimum of numbers 23,89,5 using the min() function

FUNCTION ARGUMENTS 

When defining a function in Python, we can specify parameters that act as variables to hold the inputs passed as arguments while calling that function. These functions arguments control how input apramenters are handled within the function. 

There are four types of function arguments in Python: 

1. Default Arguments
2. Required Arguments
3. Keyword Arguments
4. Variable-lenght Arguments

"""

###DEFAULT ARGUMENTS FUNCTIONS 
""""Default arguments allow default value to be used for a paramenter if no argument is passed for it. This makes invoking functions easier when some parameters are optionally speecified.
"""

# FUNCTION DEFINTION USING DEFAULT ARGUMENTS: 

def full_name (first_name,last_name,middle_name=""):
    name = first_name + ""+middle_name+""+last_name
    return name

print ("here the middle name paramenter has a default empty string value specified. So we can call the function with or withouht passing the middle namel")

print(full_name("John","Doe")) # John Doe
print(full_name("Sara","Williams","Marie"))

print("\n as we can se default arguments increase flexibility while calling functions in python ")

### REQUIRED ARGUMENTS FUNCTIONS 

print("Required arguments, as the name suggests, are paramenters thar must be passed values for while calling the function. not passing these required arguments will result in errors Here is how we define and call functions using required arguments: ")

def power(base,exponent): 
    result = base **exponent
    print(f"{base} raised to power {exponent} is {result}")
    
power(2,3)

# Insert this example we are not passing totally the required arguments exponent power(2)

"""So for required paramenters, values must be passed while invocation otherwise error will occur"""

##KEYWORD ARGUMENTS 

print("\n keyword arguments allow function paramenters to be passed values bu name at call time specifically. This provides more readeability with argument order independence.")

def student_details (name,age,class_level): 
    print(name,age,class_level)
    
student_details("Jim",16,10)


#student_details(name="Jim", age=16)

#This enhanes readabiltiy by not needing to worry about argument order, Kewyrd argas alsoallow selective param passing.

#VARIABLE- LENGHT ARGUMENTS

print("\n Variable-length args allow arbitrary number of arguments to be directly passed grupued together at call time. Common ones are- ")

print("\n *args- accepts variable number of non keyword arguments")

print("\n **kwargs- Accepts variable number of keywords arguments")

print("Usage example: ")

def total_sums(*args):
    sum = 0 
    for num in args: 
        sum+=num
        return sum
print(total_sums(1,5,8))

### The argments take in as numeric arguments as provided. Simularl we can use **Kwargs to get a dict of a keyword arguments

print("The *args take in as numeric arguments as provided. Similarly we can use **kwargs to get a dict of keyword arguments")

def user_details(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
        
#user_details(name"Lisa", age=25, gender="Female")
#Prints:
#name: Lisa
#age: 25
#gender: female

'''So in esecense, variable-length arguments orivude flexibility to pass arbitrary number of arguments to fuctions in python 

Excercises 
1.- Define a function exponent () to calculate the exponent of a number using default, rquired and keyword arguments. Call it to find 2exp4 and 3exp3.
2.- Define a sum_all() function using *args to find the sum of a variable number of integers passed to it.'''

 
#Method 1: Using default arguments
def exponent_default(base,exponent=2):
#"""calculates power with default exponent(square if not specified)
#- base: required argument
#- exponen: default argument (default to 2)"""

    return base**exponent

#METHOD 2: Using required arguments only 
def exponent_required (base,exponent):
        ##both arguments are required
    return base ** exponent 

#METHOD 3: Using keywords arguments
def exponent_keyword(base,exponent):
    ##can be called with keywrds arguments
    return base ** exponent_default

#METHOD 4: Using all three types in one function 
def exponent_all (base, exponent=2,**kwargs): 
    '''Demostrates all three arguments types: 
    -base: required positiona argument
    - exponent: default argument
    -**'''
#Using Kwargs for additional features
    if kwargs.get('show_opertion',False):
        printf("Calculating{base}^{exponent}={result}")
    if kwarg.get('round_result'):
        result = round (result, kwarg ['round_result'])
    return result

#TESTING THE FUNCTIONS

#print("=" ¨50)
print("EXCERCISE 1: exponent Function")
print("=" * 50)
      
# 1. USING DEFAULT ARGUMENTS 
print("Using default arguments function:")
print(f"2^4={exponent_default(2,4)}") # 2^4=16
print(f"3^3={exponent_default(3,3)}") # 3^3=27
print(f"5^2= (using default exponent) = {exponent_dafault(5)}") # 5^2=25 (default exponent) 
    
#2. USING REQUIRED ARGUMENTS 
print("\n2 using Required arguments: ")
print(f"2^4 = {exponent_required(2,4)}") #16
print(f"3^3 = {exponent_required(3,3)}") #27

#3. USING KEYWORD ARGUMENTS
print("\n3. Using KEYWORD arguments: ")
print(f"2^4 = {exponent_keyword(base=2,exponent=4)}")
print(f"3^3 = {exponent_keyword(exponent=3,base=3)}") #27 (order doesn't matter)

# 4. USING ALL THREE TYPES WITH ADDITIONAL FEATURES

print("\n4. Using ALL argumen types with **kwargs: ")
result1= exponent_all(2,4,show_operation=True)
result1= exponent_all(3,3,show_operation=True,round_result=2)

