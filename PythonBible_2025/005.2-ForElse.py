print("\n  ")
print(" ")

'''FOR- ELSE  a little known construct- the else block after a for loop is executed after the look ends normally

'''
for i in range(3):
    print(i)
else:
    print('loop ended')
    
#else wont run if look stops prematurely using break

#EXCERCISE 1 -  break out early from a for/else loop and observe if else runs - FOR ELSE LOOP BEHAVIOR

#example 1: Loop completes normally (else runs)
print('example 1 - loop completes normally:')
for i in range(3):
    print(f"Iteration {i}")
else:
    print(" Else clause executed (no break encountered)\n")

#Example 2: Loop breaks early (else doesn't run)
print('example 2 - Loop breaks early:')
for i in range(5):
    print(f" Iteration {i}")
    if i==2: 
        print(" Breaking at i=2")
        break
else:
    print(" This won't print because of break")
    
print()

#EXCERCISE 2: Numbers Divisible by 10
#Lets find numbers divisible by 10 from a range using IF/Else:

print ("\n === Excercise: numbers Divisible by 10 ====")

# METHOD 1 Simple filter
print("Method 1: Using modulus operator")
for num in range(1,51):
    if num % 10 ==0:
        print(f" {num} is divisible by 10")

#METHOD 2: Using step parameter in range
print("\n Method 2:using range step parameter")
for num in range(10,51,10): # start at 10, go to 50, step by 10
    print(f"{num} is divisible by 10")

#METHOD 3: With for/else to confirm finding
print("\n Method 3: With for/else validation")
search_range = range(15,26) #No multiples of 10 here

print(f"Searching range: {list(search_range)}")

for num in search_range:
    if num % 10==0: 
        print(f" Found: {num}")
        break
else:
    print("No multiples of 10 in this range")
    
# PRACTICA 1 application: Process in batches of 10
print("***********************************************")
print("\n Practica l: Processing items in batches of 10")
print("-----------------------------------------------")

items =list(range(1,101))
print(f"We have {len(items)} items to process") 
for i,item in enumerate(items,1):
    if i % 10==0:
        print(f" Processed batch up to item #{i}")
print ("fin de la lista")

print("***********************************************")
print("\n Common Patterns & Tips:")

# Pattern 1: Search with for/else

def find_first_match(items, target):
    """Find first occurence or report abscence"""
    for item in items: 
        if item == target: 
            print("f{target} found")
    else:
        print(f"{target} not found")


# Pattern 2: Validate all items
def all_positive(numbers):
    """Check if all numbers are positive."""
    for num in numbers:
        if num <= 0:
            print("Found non-positive number")
            break
    else:
        print("All numbers are positive!")
        
print("-----------------------------------------------")

# Quick test
print("\n=== Quick Tests ===")
find_first_match([1, 3, 5, 7], 5)  # Found
find_first_match([1, 3, 5, 7], 2)  # Not found
all_positive([1, 2, 3])           # All positive
all_positive([1, -2, 3])          # Found negative

"""Key Takeaways:
for/else: else runs only if loop completes without break

Divisibility check: Use num % divisor == 0

Range with step: range(start, stop, step) is efficient for patterns

Practical use: Search operations, validation, batch processing"""

#hasta aqui nos quedamos hoy https://chat.deepseek.com/share/1y0s6vhxabk42p6weo


