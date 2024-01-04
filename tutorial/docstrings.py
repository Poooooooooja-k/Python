# python docstrings are strings literals that appear right after the definition of a function,method,class or module
# docstring should be written right below the function name 
def square(n):
    '''Takes in a number n ,returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)  
