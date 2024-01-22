# virtual environment:is used to isolate specific python environments  on a single machine,allowing you to work on multiple projects with diffreent dependencies and packages without conflict

# create a virtual envirnoment
# python -m venv myenv


# activate the virtual evn
# myenv\Scripyts\activate


# importing in python program:is the processing of loading code from a python module into the current script.this helps you to use the functions and variables defined in the module into your current script
import math   

result=math.sqrt(9)
print(result)

# another method
from math import sqrt,pi
from math import *  
result=sqrt(9)*pi
print(result)

# "as" keywords
from math import sqrt as s
