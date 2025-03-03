#importing functools Module

from functools import partial

def power(base, exponent):
    return base ** exponent

# Create a new function that always raises a number to the power of 2
square = partial(power, exponent=2)

print(square(5))  # Output: 25
print(square(10)) # Output: 100
