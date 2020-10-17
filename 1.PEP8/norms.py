# PEP8 NORMS

# Guido Van Rossum: "The code is read much more often than it is written"

# Variables
# Use lowercase letters and underscores to separate words
my_var = 4

# Functions
# Use lowercase letters and underscores to separate words
def my_func():
    print("Hello")

# Classes
# Capitalize the first letter of each word — called CapWords or CamelCase
class MyClass:
    x = 5

# Constants
# All capital letters and underscores to separate words
PI_CONSTANT = 3.14

# Indentations
# 4 blanks or 1 tab

# Avoid using overly abbreviated names such as fn; write out first_name instead
# Never use lowercase ‘L’, uppercase ‘O’, or uppercase ‘I’ as variable names
# They are too easily confused with a 1 or 0

#Use those when list or arguement is long

def result = my_function(
    first_argument, second_argument,
    third_argument, fourth_argument)

def my_function(
        first_argument, second_argument,
        third_argument, fourth_argument):
    print(first_argument)

# First Character Alignment in a long list
my_list = [
    1, 2, 3,
    4, 5, 6,
]

# Use whitespace to communicate order of operations
x = 2*y + 2*z


# Keep lines under 79 characters
# Use double quotes for strings with an apostrophe
# Use single quotes for strings with quotation marks
# Always use double quotes for multiline strings

# Calculation Orders
# Don't
b = a ** 2 + 10
c = (a + b) * (a - b)
# Do
b = a**2 + 10
c = (a+b) * (a-b

# Docstrings give information when hover on function in IDE
def quadratic_formula(x, y, z, t):
    """Using the quadratic formula"""
    print("I'm in a def.")

# Lists
# Do
list = [1, 2, 3]
# Don't
list = [ 1, 2, 3, ]

# Don't leave blanks if there is no element at the array
# Do
spam = (1,)
# Don't
spam = (1, )

# Empty List is considered Falsy. So use them in True/False expression directly.
# Don't
list_value = []
if not len(list_value):
    print('LIST IS EMPTY')
# Do
list_value = []
if not list_value:
    print('LIST IS EMPTY')

# Use startswith/endswith in stringslicing
# Do
if foo.startswith('cat'):
# Don't
if foo[:3] == 'cat':
An example using .endswith():

# Don't
if file_jpg[-3:] == 'jpg':
    print('It is a JPEG image file')
# Do
if file_jpg.endswith('jpg'):
    print('It is a JPEG image file')

# Linter: pycodestyle:
# https://pypi.org/project/pycodestyle/

# AutoFormatters: Black:
# https://pypi.org/project/black/

# Multi Line Additions
# Do
income = (gross_wages

         + taxable_interest
      
         + (dividends - qualified_dividends)
      
         - ira_deduction
      
         - student_loan_interest)
# Don't
income = (gross_wages +

         taxable_interest +
      
         (dividends - qualified_dividends) -
      
         ira_deduction -
      
         student_loan_interest)

# Don't use extra spaces
# Do
spam(ham[1], {eggs: 2})
# Don't
spam( ham[ 1 ], { eggs: 2 } )

# Do
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
# Don't
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)

# Do
def complex(real, imag=0.0):
    
return magic(r=real, i=imag)
# Don't
def complex(real, imag = 0.0):

return magic(r = real, i = imag)

#Do
def munge(sep: AnyStr = None): ...

def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...
#Don't
def munge(input: AnyStr=None): ...

def munge(input: AnyStr, limit = 1000): ...

#Do
class SwapTestSuite(unittest.TestCase):

    def test_swap_operations(self):
        instance = Swap(self.a,self.b)
        value1, value2 =instance.get_swap_values()
        self.assertEqual(self.a, value2)
        self.assertEqual(self.b, value1)


class OddOrEvenTestSuite(unittest.TestCase):
    """
        This is the Odd or Even Test case Suite
    """
    def setUp(self):
        self.value1 = 1
        self.value2 = 2

# Comments should have 1 space

# PEP8 Libraryto check PEP8 compatibility
# https://pypi.org/project/pep8/1.7.1/


#Don’t surround = sign with whitespaces when indicating function parameters
def exp(base, power=2):
    return base**power

# Correct
brooklyn = [‘Amy’, ‘Terry’, ‘Gina’, 'Jake']
count = 0
for name in brooklyn:
    if name == ‘Jake’:
        print(‘Cool’)
        count += 1

# Don't. Always use is or is not
if name != None:
    print("Not null")
# Do
if name is not None:
    print("Not null")

# Use generic functions instead lambda s
# Do
def func(x):
    return None

# Don't
func = lambda x: x**2

# Comments
# Always begin the comment with a capital letter
# Comments should be complete sentences
# Update the comment as and when you update your code
# Avoid comments that state the obvious. Don't overdo it

# Block Comments
# You cant do multiline comments in python with #. One should use """"
# Describe the piece of code that follows them
# Have the same indentation as the piece of code
# Start with a # and a single space

# Inline Comments
# These are comments on the same line as the code statement
# Should be separated by at least two spaces from the code statement
# Starts with the usual # followed by a whitespace
# Do not use them to state the obvious
# Try to use them sparingly as they can be distracting


# Avoid putting whitespaces immediately within brackets
# Do
df[‘clean_text’] = df[‘text’].apply(preprocess)

# Never put whitespace before a comma, semicolon, or colon
# Do
name_split = lambda x: x.split()

Don’t include whitespaces between a character and an opening bracket
# Do
print("This is the right way")
# Do
for i in range(5):
    name_dict[i] = input_list[i]


# Trailing whitespaces should be avoided in the end of a line
# Do not surround = sign with whitespaces when indicating function parameters
# Do
def exp(base, power=2):
    return base**power

# Always surround the following binary operators with single whitespace on either side:
    # Assignment operators (=, +=, -=, etc.)
    # Comparisons (==, <, >, !=, <>, <=, >=, in, not in, is, is not)
    # Booleans (and, or, not)
# Do
brooklyn = [‘Amy’, ‘Terry’, ‘Gina’, 'Jake']
count = 0
for name in brooklyn:
    if name == ‘Jake’:
        print(‘Cool’)
        count += 1

# Write the exception type always in error handling. Dont just use Error with the type
# Do
try:
    x = 1/0
except ZeroDivisionError:
    print('Cannot divide by zero')

# All returns should be returning something. It shouldn't be blank
# Don't
def sample(x):
    if x > 0:
        return x+1
    elif x == 0:
        return
    else:
        return x-1

# Do
def sample(x):
    if x > 0:
        return x+1
    elif x == 0:
        return None
    else:
        return x-1