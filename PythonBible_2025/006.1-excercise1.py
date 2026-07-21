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