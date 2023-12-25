a=int(input("enter your age: "))
print("your age is:",a)
# conditional operators
#  >,<,>=,<=,==,!=
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)
if(a>18):
    print("you can drive")
else:
    print("you cannot drive")
appleprice=210
budget=200
if(appleprice<=budget):
    print("alexa,add 1 kg apples to the cart.")
elif(budget-appleprice>70):
    print("its okey you can buy")
else:
    print("alexa,do not add apples to the cart.")
num=18
if(num<0):
    print("number is negative")
elif(num>0):
    if (num<=10):
        print("number is between 1-10")
    elif(num>10 and num<=20):
        print("number is between 11-20")
    else:
        print("number is greather than 20")
else:
    print("number is zero")