

# Difference Between a Variable and a Constant
'''
Variables
•	Definition: A variable is a storage location identified by a name that can hold different values during the execution of a program.
•	Mutability: Variables can change their value.
•	Example:Python
x = 10
x = 20  # x now holds the value 20
'''
''''
Constants
•	Definition: A constant is a value that, once assigned, cannot be changed during the execution of a program.
•	Immutability: Constants are meant to remain the same throughout the program.
•	Example:
'''
Python
PI = 3.14159

# Constants in Python

'''Python does not have built-in support for constants like some other programming languages (e.g., const keyword in C++). However, 
by convention, you can indicate that a variable should be treated as a constant by using all uppercase letters in its name. 
This is a signal to other programmers that the value should not be changed.'''

# Example of Constants in Python

MAX_USERS = 100
PI = 3.14159

''
While you can still technically change the value of these “constants,” it is considered bad practice to do so.
Using const in Python (with a library)
For stricter enforcement, you can use a library like const:
1.	Install the library:
2.	pip install const
3.	Use it in your code:
''

# Python
from const import const
const.MAX_USERS = 100
const.PI = 3.14159

# Trying to change the value will raise an error
const.MAX_USERS = 200  # This will raise a ConstError

# Summary
•	Variables can change their values.
•	Constants are meant to remain unchanged, and in Python, this is enforced by convention or using external libraries.
