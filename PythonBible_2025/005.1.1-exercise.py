
#1. Iterate over a list of fruits and print their names
print("#Method 1: Direct List definition")
fruits = ["apple","banana","orange","grape","mango"]

print("\nFruits in the list:")
for fruit in fruits:
    print(fruit)
    
print("\n#Method 2: Using enumerate to get index and fruit name")
print("\nFruits with their positions:")
for index, fruit in enumerate(fruits):
    print(f"{index+1}.{fruit}")

print("\n#2. Print multiples of 3 from 0 to 30 using range() and for")

print("\n#Method 1: Using range with step parameter")
print("Multiples of 3 (using step):")
for number in range(0,32,3):
    print(number)

print("\n#Method 2: Using modulo operator to check mutliples ")

print("\nMultiple of 3 (using modulo):")
for number in range(0,31):
    if number % 3 ==0:
        print(number)

print("\n#Method 3: More concise version")

print("\n Multiples of 3 (concise):")        
multiples_of_3 = [num for num in range(0,31) if num % 3 ==0]
for num in multiples_of_3:
    print(num)

print("\n#COMPLETE COMBINED SOLUTION")    

print("\n#task1: fruits iteration") 
 
print("task 1 fruits iteration ")
fruits =["apple","banana","orange","grape","mango","strawberry"]    
print('===FRUITS====')
for fruit in fruits:
    print(f"-{fruit}")

print("\n#task 2: Multiples of 3")

print("\n=== MULTIPLES OF 3 ===")
for num in range (0,31,3):
    print(num)
    
print("tu casa es mi casa")
