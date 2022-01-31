import calculator

# print(add(2, 3)) This wont work as everything is packed inside the module

print(calculator.add(1, 2))
print(calculator.CONSTANT)

#############

# For filtered imports

from calculator import add

# After this calcuator wont be in scope

print(add(1, 2))

# To import all
# from calculator import *

###########

# For aliasing the import

import calculator as calc

print(calc.add(1, 2))
