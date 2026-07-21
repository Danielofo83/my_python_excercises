# METHOD 1: Using default arguments
def exponent_default(base, exponent=2):
    """
    Calculates power with default exponent (square if not specified)
    - base: required argument
    - exponent: default argument (defaults to 2)
    """
    return base ** exponent

# METHOD 2: Using required arguments only
def exponent_required(base, exponent):
    """
    Both arguments are required
    """
    return base ** exponent

# METHOD 3: Using keyword arguments
def exponent_keyword(base, exponent):
    """
    Can be called with keyword arguments
    """
    return base ** exponent

# METHOD 4: Using all three types in one function
def exponent_all(base, exponent=2, **kwargs):
    """
    Demonstrates all three argument types:
    - base: required positional argument
    - exponent: default argument
    - **kwargs: keyword arguments (for additional options)
    """
    result = base ** exponent
    
    # Using kwargs for additional features
    if kwargs.get('show_operation', False):
        print(f"Calculating {base}^{exponent} = {result}")
    
    if kwargs.get('round_result'):
        result = round(result, kwargs['round_result'])
    
    return result

# TESTING THE FUNCTIONS
print("=" * 50)
print("EXERCISE 1: Exponent Function")
print("=" * 50)

# 1. Using default argument function
print("\n1. Using DEFAULT arguments:")
print(f"2^4 = {exponent_default(2, 4)}")      # 16
print(f"3^3 = {exponent_default(3, 3)}")      # 27
print(f"5^2 (using default exponent) = {exponent_default(5)}")  # 25

# 2. Using required arguments
print("\n2. Using REQUIRED arguments:")
print(f"2^4 = {exponent_required(2, 4)}")     # 16
print(f"3^3 = {exponent_required(3, 3)}")     # 27

# 3. Using KEYWORD arguments
print("\n3. Using KEYWORD arguments:")
print(f"2^4 = {exponent_keyword(base=2, exponent=4)}")     # 16
print(f"3^3 = {exponent_keyword(exponent=3, base=3)}")     # 27 (order doesn't matter)

# 4. Using all three types with additional features
print("\n4. Using ALL argument types with **kwargs:")
result1 = exponent_all(2, 4, show_operation=True)
result2 = exponent_all(3, 3, show_operation=True, round_result=2)
print(f"3.14159^2 with rounding = {exponent_all(3.14159, round_result=2)}")

# 5. Creating a single function that handles all cases
def flexible_exponent(*args, **kwargs):
    """
    Ultra-flexible exponent function
    Can handle different calling methods
    """
    if len(args) == 1:
        base = args[0]
        exponent = kwargs.get('exponent', 2)
    elif len(args) == 2:
        base, exponent = args
    else:
        base = kwargs.get('base', 0)
        exponent = kwargs.get('exponent', 2)
    
    result = base ** exponent
    
    if kwargs.get('verbose'):
        print(f"{base} raised to {exponent} = {result}")
    
    return result

print("\n5. Using FLEXIBLE function:")
print(f"2^4 = {flexible_exponent(2, 4)}")
print(f"3^3 = {flexible_exponent(base=3, exponent=3)}")
print(f"5^2 = {flexible_exponent(5)}")
print(f"4^3 (verbose) = {flexible_exponent(4, 3, verbose=True)}")


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

# Complete program to test both exercises
def main():
    print("\n" + "=" * 60)
    print("FUNCTIONS EXERCISES - COMPLETE SOLUTION")
    print("=" * 60)
    
    # EXERCISE 1: Exponent function
    print("\n📌 EXERCISE 1: Exponent Function")
    print("-" * 40)
    
    # Required for the specific calls: 2^4 and 3^3
    print("Specific calls requested:")
    print(f"2^4 = {exponent_required(2, 4)}")
    print(f"3^3 = {exponent_required(3, 3)}")
    
    print("\nAdditional examples:")
    print(f"2^4 (keyword args) = {exponent_keyword(base=2, exponent=4)}")
    print(f"3^3 (keyword args) = {exponent_keyword(exponent=3, base=3)}")
    print(f"5^3 = {exponent_default(5, 3)}")
    print(f"4^2 (using default) = {exponent_default(4)}")
    
    # EXERCISE 2: Sum All function
    print("\n📌 EXERCISE 2: Sum All Function")
    print("-" * 40)
    
    print(f"sum_all_basic(1, 2, 3, 4, 5) = {sum_all_basic(1, 2, 3, 4, 5)}")
    print(f"sum_all_basic(10, 20, 30) = {sum_all_basic(10, 20, 30)}")
    print(f"sum_all_basic(2, 4, 6, 8) = {sum_all_basic(2, 4, 6, 8)}")
    print(f"sum_all_basic(1, 1, 1, 1, 1, 1, 1) = {sum_all_basic(1, 1, 1, 1, 1, 1, 1)}")
    
    # Bonus: Combining both exercises
    print("\n🎯 BONUS: Combining both functions")
    print("-" * 40)
    numbers = [2, 3, 4]
    exponents = [4, 3, 2]
    
    for num, exp in zip(numbers, exponents):
        power = exponent_required(num, exp)
        print(f"{num}^{exp} = {power}")
    
    sum_of_powers = sum_all_basic(*[exponent_required(2,4), exponent_required(3,3)])
    print(f"Sum of 2^4 + 3^3 = {sum_of_powers}")

# Run the main function
if __name__ == "__main__":
    main()