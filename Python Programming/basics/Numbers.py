x = 4

float(x)
 
y = 2.0
int(y)

a = 2**2

b = 2 ** 10000

result = 1/3.0
# precision
# repr, str, print

# comparison
# ==, !=, >, <, >=, <=

import math
math.floor(3.5)
math.floor(-3.45)

math.trunc(2.8) # closest towards zero
math.trunc(-2.8) # closest towards zero

# complex numbers
# 2 + 3j 

0o20 # octal
0x10 # hexadecimal
0b10 # binary

oct(64)
hex(64)
bin(64)


int('64', 8) # 64 to octal
int('10', 2) # 10 to binary


# Bitwise operation
x = 1
x << 2 # left shift


import random
random.random()

random.randint(1, 10)

random.choice([1, 2, 3, 4, 5])

random.shuffle([1, 2, 3, 4, 5])

from decimal import Decimal
Decimal('0.1') + Decimal('0.2') - Decimal('0.3')

# Fractions
from fractions import Fraction
Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3)

# sets
a = {1,2,3,4,5}
b = {3,4,5,6,7}
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
a.issubset(b)
a.issuperset(b)

