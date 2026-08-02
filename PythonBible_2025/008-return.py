'''the return statement is used to exit a function and return a value to the caller. When a return statement is executed, the function terminates immediately, and the specified value is sent back to the caller. If no value is specified, the function returns None by default. The return statement can be used to return any type of value, including numbers, strings, lists, dictionaries, or even other functions. It allows functions to produce output that can be used in other parts of the program.This enables assigning functions execution results to variables for further processing.'''

def add_nums(num1,num2):
    sum = num1 + num2
    return sum

result = add_nums(5, 10)
print("The sum is:", result)  # Output: The sum is: 15

'''When return sum executes inside add_nums, value of sum is sent black.
This output is assigned to result variable and printed

Some keypoints about the return statement:
1. A function terminates execution immediately after return stamt
2. Value following return like further statements wont be executed
3. If no value is specified, function returns None by default
4. Return statement can be used to return any type of value, including numbers, strings, lists,     dictionaries, or even other functions.
5. Can return multiple values as a tuple, which can be unpacked by the caller'''

#TERMINATES FUNCTION EXECUTION 

def add_sub(num1, num2):
    sum = num1 + num2
    difference = num1 - num2
    return sum, difference

print(add_sub(5, 3)) # Returning multiple values as a tuple

#RETURN NONE IF NO RETURN VALUE:
def print_name(name):
    print("Hello,", name)
    
print(print_name("Alice"))  # Output: Hello, Alice
'''since no return statemnet, print name returns None implicitly. When we print the result of print_name, it displays None after printing the greeting.
'''
#RETURN ULTIPLE VALUES AS A TUPLE
def min_max(nums):
    minimum = min(nums)
    maximum = max(nums)
    return minimum, maximum

min,max = min_max([3, 1, 4, 1, 5, 9])
print("Minimum:", min)  # Output: Minimum: 1
print("Maximum:", max)  # Output: Maximum: 9
'''so in summary return statement returns execution control back to caller code while also sending function outputs. Properly using returns is vital for reusable modular functions.
'''


#PLEASE FIND BELOW EXCERCISES 

'''1. define a currency convertes function rom usd to EUR. USe retur statement properly and call this function to get the converted EUR value for 10 USD
2. define a fuction to return multiple value (name, age) for a user passed. call it for name ="Sam" and age =25'''

#excise part one 
def usd_to_eur(usd_amount, exchange_rate=0.85):
    """
    Convert USD to EUR
    
    Args:
        usd_amount: Amount in USD
        exchange_rate: Current USD to EUR exchange rate (default 0.85)
    
    Returns:
        Converted amount in EUR
    """
    eur_amount = usd_amount * exchange_rate
    return eur_amount

# Call the function for 10 USD
usd_value = 10
eur_value = usd_to_eur(usd_value)

print(f"{usd_value} USD is equal to {eur_value:.2f} EUR")

# You can also call it with a custom exchange rate
custom_rate = 0.92
eur_with_custom_rate = usd_to_eur(10, custom_rate)
print(f"With exchange rate {custom_rate}, {usd_value} USD = {eur_with_custom_rate:.2f} EUR")


#excercise part two

def get_user_info(name, age):
    """
    Return user information as multiple values
    
    Args:
        name: User's name
        age: User's age
    
    Returns:
        Tuple containing (name, age)
    """
    # You can do some processing here if needed
    formatted_name = name.title()  # Capitalizes first letter
    age_next_year = age + 1
    
    # Return multiple values as a tuple
    return formatted_name, age_next_year

# Call the function for Sam, age 25
user_name = "Sam"
user_age = 25

# Method 1: Unpack the returned values directly
name_result, age_result = get_user_info(user_name, user_age)
print(f"Name: {name_result}, Age: {age_result}")

# Method 2: Store the entire returned tuple
user_data = get_user_info(user_name, user_age)
print(f"User data as tuple: {user_data}")
print(f"Name from tuple: {user_data[0]}")
print(f"Age from tuple: {user_data[1]}")

# Method 3: Using the function directly in print
print(f"Direct call: {get_user_info('Sam', 25)}")


'''Returning Values Functions don't have to just perform tasks; they can also return values. To return a value from a function, you use the return keyword followed by the value you want to return. Here's an example: '''

def square(x): 
    return x ** 2 
result = square(5) 
print(result) 
    

'''# outputs 25 This function takes in a parameter x and returns its square. The value returned by the function is assigned to the variable result, which is then printed to the console.'''

'''Multiple Return Values Functions can also return multiple values. To do this, you simply separate the values you want to return with commas.'''
# Here's an example: 

def divide(x, y):
quotient = x // y 
remainder = x % y 
return quotient, remainder 
result1, result2 = divide(10, 3) 
print("\n")

print(result1) # outputs 3 
print(result2) # outputs 1 


'''This function takes in two parameters x and y and returns their quotient and remainder. The values returned by the function are assigned to two variables result1 and result2, which are then printed to the console. assigned to two variables result1 and result2, which are then printed to the console.'''