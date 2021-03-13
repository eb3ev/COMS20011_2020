import sys
import numpy as np

def product(numbers):
    if len(numbers) != 2:
        return number
    return float(numbers[0]) * float(numbers[1])
        
numbers = sys.argv[1:]
print(product(numbers))
