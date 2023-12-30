# default arguments:provides a default value while creating a function

# keyword arguments:provides arguments with a key-value,this way the interpreter recognizes the arguments by the parameter name 
# the order in which the parameter is passed doesnit matter

# variable length arguments:

# keyword arbitart arguments:the function accesses the arguments by processing them in the form of dictionary

# required arguments:Incase we dont pass the argumnets in the key-value syntax,then it is necessary to pass the arguments in the correct positional order and 
# the number of argumnets passed should match with the actual parameter


# default
def average(a=9,b=1):
    print("the average is ",(a+b)/2)
# average(4,6)
average(5)

# keyword
def name(fname,mname,lname):
    print("hello,",fname,mname,lname)
name(mname="peter",lname="wesker",fname="jade")

# required
def average(a,b,c=1):
    print("the average is ",(a+b+c)/2)
average(5,6)

# variable-length
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    print("average is:",sum/len(numbers))

def name(**name):
    print("hello,",name["fname"],name["mname"],name["lname"])
name(mname="peter",lname="wesker",fname="jade")



# return statement is used to return the value of the expression back to the calling function
def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)