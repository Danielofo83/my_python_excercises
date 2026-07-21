# METHOD 1: Basic *args implementation
def sum_all_basic(*args):
    """
    Sums all numbers passed as arguments
    *args allows any number of positional arguments
    """
    total = 0
    for number in args:
        total += number
    return total

# METHOD 2: Using built-in sum() function
def sum_all_pythonic(*args):
    """
    More Pythonic way using the built-in sum() function
    """
    return sum(args)

# METHOD 3: With type checking and error handling
def sum_all_safe(*args):
    """
    Includes type checking and error handling
    Only sums numbers, ignores non-numeric values
    """
    total = 0
    numbers_count = 0
    
    for item in args:
        if isinstance(item, (int, float)):
            total += item
            numbers_count += 1
        else:
            print(f"Warning: '{item}' is not a number and will be ignored")
    
    print(f"Sum of {numbers_count} numbers: ", end="")
    return total

# METHOD 4: Advanced version with filtering
def sum_all_advanced(*args, **kwargs):
    """
    Advanced version with additional features
    - *args: variable numbers to sum
    - **kwargs: additional options
    """
    # Filter only numeric values
    numbers = [x for x in args if isinstance(x, (int, float))]
    
    if kwargs.get('ignore_negatives', False):
        numbers = [x for x in numbers if x >= 0]
    
    if kwargs.get('only_integers', False):
        numbers = [x for x in numbers if isinstance(x, int)]
    
    total = sum(numbers)
    
    if kwargs.get('verbose', False):
        print(f"Numbers to sum: {numbers}")
        print(f"Count: {len(numbers)}")
        
    return total

# TESTING THE FUNCTIONS
print("\n" + "=" * 50)
print("EXERCISE 2: Sum All Function with *args")
print("=" * 50)

# 1. Testing basic version
print("\n1. BASIC *args version:")
print(f"sum_all_basic(1, 2, 3, 4, 5) = {sum_all_basic(1, 2, 3, 4, 5)}")           # 15
print(f"sum_all_basic(10, 20) = {sum_all_basic(10, 20)}")                         # 30
print(f"sum_all_basic(2, 4, 6, 8, 10, 12) = {sum_all_basic(2, 4, 6, 8, 10, 12)}") # 42

# 2. Testing Pythonic version
print("\n2. PYTHONIC version (using sum()):")
print(f"sum_all_pythonic(1, 2, 3) = {sum_all_pythonic(1, 2, 3)}")                 # 6
print(f"sum_all_pythonic(5, 10, 15, 20) = {sum_all_pythonic(5, 10, 15, 20)}")     # 50

# 3. Testing with different numbers of arguments
print("\n3. Testing with DIFFERENT numbers of arguments:")
print(f"2 arguments: sum_all_basic(5, 7) = {sum_all_basic(5, 7)}")                # 12
print(f"3 arguments: sum_all_basic(1, 2, 3) = {sum_all_basic(1, 2, 3)}")          # 6
print(f"5 arguments: sum_all_basic(1, 1, 1, 1, 1) = {sum_all_basic(1, 1, 1, 1, 1)}") # 5
print(f"0 arguments: sum_all_basic() = {sum_all_basic()}")                        # 0

# 4. Testing with type checking
print("\n4. Testing with TYPE CHECKING:")
print(f"sum_all_safe(1, 2, 'hello', 3, True) = {sum_all_safe(1, 2, 'hello', 3, True)}")

# 5. Testing advanced version with kwargs
print("\n5. Testing ADVANCED version with options:")
numbers = [5, -3, 10, -1, 7, 2.5, 3]
print(f"All numbers: {numbers}")
print(f"Regular sum: {sum_all_advanced(*numbers)}")
print(f"Ignore negatives: {sum_all_advanced(*numbers, ignore_negatives=True)}")
print(f"Only integers: {sum_all_advanced(*numbers, only_integers=True)}")
print(f"Verbose mode:")
sum_all_advanced(*numbers, verbose=True, ignore_negatives=True)

# 6. Practical examples
print("\n6. PRACTICAL EXAMPLES:")

# Example: Calculating average
def calculate_average(*grades):
    """Calculate average of grades using sum_all"""
    if len(grades) == 0:
        return 0
    total = sum_all_basic(*grades)
    return total / len(grades)

student_grades = [85, 90, 78, 92, 88]
print(f"Grades: {student_grades}")
print(f"Average: {calculate_average(*student_grades):.2f}")

# Example: Shopping cart total
def shopping_cart_total(*prices):
    """Calculate total price of items in cart"""
    subtotal = sum_all_basic(*prices)
    tax = subtotal * 0.07  # 7% tax
    total = subtotal + tax
    return f"Subtotal: ${subtotal:.2f}, Tax: ${tax:.2f}, Total: ${total:.2f}"

print(f"\nShopping cart: {shopping_cart_total(25.99, 12.50, 5.75)}")
