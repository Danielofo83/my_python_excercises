print("\n  ")
print(" ")

#Excercise 1.Practice creating differents lists, tuples and dictionaries, accessing and printing their values
#1.1.Lists (mutable ordered sequences)
#Creating lists 

#1.1.1 empty list 

empty_list = []
print(empty_list)

#1.1.2 List of integers
numbers=[1,2,3,4,5]
print(numbers)

#1.1.3 Mixed Datatypes
mixed_list = [10,'hello',3.14,True]
print(mixed_list) #[10,'hello',3.14,True]

#1.1.4 List from range
range_list =list(range(5)) #0,1,2,3,4
print(range_list)


#1.2 Accessing to the List elements
fruits = ['apple','bannana','cherry','date']
print(fruits)

#1.2.1 Positive Indexing
print(fruits[0])#Apple
print(fruits[2])# Cherry

#1.2.2 Negative indexing
print(fruits[-1])#date
print(fruits[-2])#cherry

#1.2.3 Slicing
print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])

#1.3 Modifying Lists
colors =['red','green','blue']

#1.3.1 Changing elements
colors[1]='yellow'
print(colors) # red, yellow, blue

#1.3.2 Appending 
colors.append('purple')
print(colors)

#1.3.3 Inserting
colors.insert(1,"dark blue")
print(colors)

#1.3.4 remove
colors.remove('yellow')
print(colors)

#2. TUPLES (INMUTABLE ORDERED SEQUENCES)

#2.1 CREATING TUPLES
#2.1.1 empty tuple
empty_tuple = ()
print(empty_tuple) #()

#2.1.2 single-element tuple (note the comma)
single_tuple = (42,)
print(single_tuple) #42

#2.1.3 Multiple elements
coordinates = (10.5,20.3) #(10.5, 20.3)

#2.1.4 without parentheses (tuple packing)
packed = 1,2,3
print(packed) #,1,2,3

#2.2 ACCESSING TUPLE ELEMENTS
dimensions = (1920, 1080, "HD")

#2.2.1 Indexing
print(dimensions[0])  # 1920
print(dimensions[-1])  # "HD"

#2.2.2 Slicing
print(dimensions[:2])  # (1920, 1080)

#2.2.3 Tuple unpacking
width, height, quality = dimensions
print(f"Width: {width}, Height: {height}")  # Width: 1920, Height: 1080

#2.3 Tuples are inmutable
#this will cause an error
#dimnsions [0] =2560

#3.DICTIONARIES (MUTABLE KEY-VALUE PAIRS)

#3.1 CREATING DICTIONARIES

#3.1.1 Empty dictionary
empty_dict = {}
print(empty_dict) # {}

#3.1.2 with key-value pairs

person = {
    'name':'Alice',
    'age':30,
    'is_student':False
}
print(person) #{ name: "Alice", age: 30,is_student: false

#3.1.3 using dict() constructor

scores = dict(math=90,science=80,history=78)

#3.2 ACCESING DICTIONARIES VALUES

#3.2.1 Get values by key

print(person['name'])
print(scores['math'])

#3.2.2 using get() to avoid KeyError

print(person.get('age')) #30
print(person.get("address","Not specified")) #"Not specified" (default)

#3.2.3 All Keys and values

print(person.keys()) #dict_keys(['name', 'age', 'is_student'])
print(person.values()) #dict_values(['Alice', 30, False])

#3.3 MODIFIYING DICTIONARIES

#3.3.1 adding new key-value pair
person["email"]="alice@example.com"
print(person) #Now includes email
print(person.keys())

#3.3.2 updating value
person["age"]=31
print(person["age"]) #31

#3.3.3 Removing items
del person["is_student"]
print(person)#removed is_student

#3.3.4update multiple items
person.update({"city": "New York", "age": 32})
print(person)

#3.4 Dictionary Iteration

#3.4.1 Iterate through keys
for key in person:
    print(key,":",person[key])


#3.4.2 iterate through items
for key, value in person.items():
    print(f"{key}:{value}")

#3.5 PRACTICAL EXAMPLE COMBINING ALL THREE

#3.5.1 a student database example below:

students = [
    {"id":101,
    "name":"John",
    "grades":(85,90,78),
    "subjects":["Math","Physics","chemistry"]
    },
    {"id":102,
       "name":"Emma",
       "grades":(92,88,95),
       "subjects":["Biology","History","English"]
    }
]
#3.5.2 Accesing nested data
print(students[0]["name"])#John
print(students[1]["grades"][1]) #88
print(students[0]["subjects"][-1]) #chemistry

#3.5.3 adding a new student
students.append({
    "id":103,
    "name":"Alex",
    "grades":(78,85,80),   
    "subjects":["art","music","Geography"]
})

#Excercise 2.Try modifying lists by adding,changing and removing elements with different methods. Observe errors with tuples
#Modifying Lists vs. Tuples: A Hands-On Exploration
#List Modification (Mutable)
#2.1 adding elements

colors = ["red","green","blue"]

#2.1.1 append() - adds to the end
print(colors) #['red', 'green', 'blue']

#2.1.2 insert() - adds at specific position
colors.insert(1,"orange")
print(colors)#['red', 'orange', 'green', 'blue']

#2.1.3 extend() - adds multiple elements
colors.extend(["purple","pink"])
print(colors) #['red', 'orange', 'green', 'blue', 'purple', 'pink']

#2.1.4 + operatr - concatenates list 
more_colors = colors +["cyan","magenta"]
print(more_colors) #['red', 'orange', 'green', 'blue', 'purple', 'pink', 'cyan', 'magenta']

#2.2 Changing Elements 
#2.2.1 direct index assignment
colors[2]="line"
print(colors) #['red', 'orange', 'line', 'blue', 'purple', 'pink']

#2.2.2 Slicing assignment
print(colors)
colors[1:3]=["amber","teal","violet"] #Replaces 2 elements with 3
#['red', 'amber', 'teal', 'violet', 'blue', 'purple', 'pink']
print (colors)

#2.2.3 step in slicing

numbers = [1,2,3,4,5,6]
print(numbers)
numbers[1::2]=[20,40,60] # Replace every other element starting at index 1
print(numbers) # [1, 20, 3, 40, 5, 60]

#2.3 Removing Elements

#2.3.1 remove() - by value
print(colors)
colors.remove("blue") #removes value of blue
print(colors) #remove first ocurrence of blue

#2.3.2 pop - by index (returns removed value)
removed =colors.pop(3)
print(f"Removeded {removed}, remainig: {colors}")


#2.3.3 del statement
del colors[0:2]  # Remove slice
print(colors)  # ['violet', 'yellow', 'purple', 'pink']

#2.3.4 clear() - empty the list
colors.clear()
print(colors)  # []

#2.3.4 Tuple Modification Attems(inmutable errors)
#2.3.4 Adding elements
dimensions = (1920, 1080)

try:
    dimensions.append(60)  # AttributeError
except AttributeError as e:
    print(f"Error: {e}")  # 'tuple' object has no attribute 'append'

try:
    dimensions += (60,)  # Actually creates a new tuple
    print("This works but creates new tuple:", dimensions)
except Exception as e:
    print(f"Error: {e}")

#2.3.5 Changing elements
"""gb = ("red", "green", "blue")

try:
    rgb[1] = "yellow"  # TypeError
except TypeError as e:
    print(f"Error: {e}")  # 'tuple' object does not support item assignment

try:
    rgb[0:2] = ("cyan", "magenta")  # TypeError
except TypeError as e:
   print(f"Error: {e}")
    
#2.3.6 Removing elements
days = ("Mon", "Tue", "Wed")

try:
    days.remove("Tue")  # AttributeError
except AttributeError as e:
    print(f"Error: {e}")  # 'tuple' object has no attribute 'remove'

try:
    del days[1]  # TypeError
except TypeError as e:
    print(f"Error: {e}")  # 'tuple' object doesn't support item deletion
"""
#2. 3.6 Workarounds for Tuples
#Since tuples are immutable, you need to create new tuples to "modify" them:
# Adding elements
original = (1, 2, 3)
new_tuple = original + (4,)  # Comma makes it a tuple
print(new_tuple)  # (1, 2, 3, 4)

# "Modifying" elements
rgb = ("red", "green", "blue")
modified_rgb = (rgb[0], "yellow", rgb[2])
print(modified_rgb)  # ('red', 'yellow', 'blue')

# "Removing" elements
days = ("Mon", "Tue", "Wed", "Thu")
new_days = days[:2] + days[3:]  # Skip index 2
print(new_days)  # ('Mon', 'Tue', 'Thu')

"""Key Observations:
Lists are fully mutable - you can change, add, and remove elements freely

Tuples are immutable - any modification attempt raises an error

To "modify" a tuple, you must create a new tuple with the desired changes

Common errors when trying to modify tuples:

AttributeError for methods like append/remove

TypeError for item assignment/deletion

This immutability makes tuples useful for:

Data that shouldn't change (constants, configuration)

Dictionary keys (which require immutable types)

Performance optimization (tuples are faster than lists)"""

#Exercise 3- Create a custom dictionary mapping product names to prices. Practice accesing, updating and adding key-value pairs.
#1. Creating the Product Dictionary
# Initialize an empty product dictionary
products = {}

# Add products with their prices
products["Laptop"] = 999.99
products["Smartphone"] = 699.99
products["Headphones"] = 149.99
products["Mouse"] = 24.99

# Alternative initialization with values
products = {
    "Laptop": 999.99,
    "Smartphone": 699.99,
    "Headphones": 149.99,
    "Mouse": 24.99
}

print("Initial Product Catalog:")
print(products)

#2. Accessing Values
# Accessing prices directly
print("\nPrice Checks:")
print(f"Laptop price: ${products['Laptop']}")
print(f"Headphones price: ${products.get('Headphones')}")

# Safe access with default value
print(f"Tablet price: ${products.get('Tablet', 'Product not found')}")

# Get all products or prices
print("\nAll Products:", list(products.keys()))
print("All Prices:", list(products.values()))

#3 Updating Prices
# Accessing prices directly
print("\nPrice Checks:")
print(f"Laptop price: ${products['Laptop']}")
print(f"Headphones price: ${products.get('Headphones')}")

# Safe access with default value
print(f"Tablet price: ${products.get('Tablet', 'Product not found')}")

# Get all products or prices
print("\nAll Products:", list(products.keys()))
print("All Prices:", list(products.values()))

#4. Adding New Products
# Add new products
products["Keyboard"] = 49.99
products.update({"Monitor": 199.99, "Webcam": 89.99})

print("\nExpanded Catalog:")
print(products)

# Adding with user input
new_product = input("\nEnter a new product name: ")
new_price = float(input("Enter its price: "))
products[new_product] = new_price

#5. Removing Products
# Remove a product
del products["Mouse"]
removed = products.pop("Webcam", None)  # Safe removal

print("\nAfter Removals:")
print(products)

# Clear all products (commented out to keep our data)
# products.clear()

#6.Advanced Operations
# Price adjustment for all products
print("\nApplying 5% price increase:")
for product in products:
    products[product] *= 1.05

# Finding products in price range
min_price = 50
max_price = 500
affordable = {p: pr for p, pr in products.items() if min_price <= pr <= max_price}

print(f"\nProducts between ${min_price}-${max_price}:")
print(affordable)

# Sorting products by price
print("\nProducts sorted by price:")
for product, price in sorted(products.items(), key=lambda item: item[1]):
    print(f"{product:12}: ${price:8.2f}")
    
    #7. Error handling examples
    # Trying to access non-existent key
try:
    print(products["Tablet"])
except KeyError:
    print("\nError: Tablet not in catalog")

# Trying to add invalid price
try:
    products["Charger"] = "twenty dollars"
except ValueError:
    print("Error: Price must be a number")
    
#PRACTICAL APPLICATION EXAMPLE BELOW
# Shopping cart simulation
cart = ["Laptop", "Headphones", "Mouse"]
total = sum(products[item] for item in cart if item in products)

print(f"\nCart Total: ${total:.2f}")

# Apply discount for expensive purchases
if total > 1000:
    total *= 0.9  # 10% discount
    print("Discount applied! New total:", f"${total:.2f}")
    
    """This comprehensive exercise covers all fundamental dictionary operations while working with a practical product-price mapping scenario. You can extend this further by:

Adding product categories or descriptions

Creating inventory counts

Building a simple shopping system

Saving/loading the dictionary to/from a file"""