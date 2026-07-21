"""In Python, documentation strings or docstrings allow functions, modules, classes etc. to have associated metadata descriptions. These provide crucial insight into component purpose, usage, parameters, outputs etc. directly in the source code itself."""
def print_line():
    print("-----------------------------------------------------")
    
    print(print_line-__doc__)

print("la funcion ya fue declarada")

# 1 EJERCICIO NUMERO UNO PARA DOCSTRINGS 

def find_maximum_of_three(a, b, c):
    """
    Return the maximum value among three given numbers.
    
    This function compares three numerical values and returns the largest one.
    It handles integers, floats, or mixed numeric types. When two or more
    numbers are equal and tie for the maximum, that value is returned.
    
    Parameters
    ----------
    a : int or float
        The first number to compare.
    b : int or float
        The second number to compare.
    c : int or float
        The third number to compare.
    
    Returns
    -------
    int or float
        The maximum value among the three input numbers. The return type
        matches the type of the largest number.
    
    Examples
    --------
    >>> find_maximum_of_three(5, 10, 3)
    10
    
    >>> find_maximum_of_three(7.5, 2.3, 9.8)
    9.8
    
    >>> find_maximum_of_three(-1, -5, -3)
    -1
    
    >>> find_maximum_of_three(4, 4, 2)
    4
    
    >>> find_maximum_of_three(0, 0, 0)
    0
    """
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
    
print("la segunda funcion esta corriendo correctamente")


#ALTERNATIVE IMPLEMENTATION WITH NYMPY-STYLE DOCSTRING

def find_maximum_of_three_numpy_style(a, b, c):
    """
    Return the maximum value among three given numbers.
    
    Compares three numerical values and returns the largest one.
    Handles integers, floats, or mixed numeric types.
    
    Parameters
    ----------
    a : {int, float}
        First number for comparison
    b : {int, float}
        Second number for comparison
    c : {int, float}
        Third number for comparison
    
    Returns
    -------
    max_value : {int, float}
        The maximum value among a, b, and c
    
    Raises
    ------
    TypeError
        If any argument is not a numeric type (int or float)
    
    See Also
    --------
    builtins.max : Python's built-in function for finding maximum values
    
    Examples
    --------
    >>> find_maximum_of_three_numpy_style(25, 18, 32)
    32
    
    >>> find_maximum_of_three_numpy_style(3.14, 2.71, 1.41)
    3.14
    
    >>> find_maximum_of_three_numpy_style(-5, -2, -8)
    -2
    """
    # Input validation (optional but recommended)
    for name, value in [('a', a), ('b', b), ('c', c)]:
        if not isinstance(value, (int, float)):
            raise TypeError(f"Parameter '{name}' must be int or float, got {type(value).__name__}")
    
    # Find and return maximum
    return a if (a >= b and a >= c) else (b if (b >= c) else c)

print("se ha ejecutado la siguiente opcion ALTERNATIVE IMPLEMENTATION WITH NUMPU-STYLE Docstring")
