# a function is a block of block that performs a specific task when it is called
def calculategmean(a,b):
    mean=(a*b)/(a+b)
    print(mean)
def isgreather(a,b):
    if(a>b):
        print("first number is greather")
    else:
        print("second number is greather")
def islesser(a,b):
    pass
# pass is used when you want to write the function body later
a=9
b=8
calculategmean(a,b)
isgreather(a,b)
c=8
d=7
calculategmean(c,b)
isgreather(c,d)
# build in functions:pre-coded in python
# min(),max(),len(),sum(),type(),range(),dict(),list(),tuple(),set(),print()etc
# user-defined functions-defined by the user
# we call a function by giving the function name followed by the parameters if any in the paramthesis
 
