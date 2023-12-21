print("1.addition /n 2.substractopn/n 3.multiplication /n 4.division")
num1=int(input("enter the 1st number: "))
num2=int(input("enter the 2nd number: "))
choice=int(input("enter your choice: "))
if choice==1:
    out=num1+num2
    print("output for addition is:",out)
elif choice==2:
    out=num1-num2
    print("output for substraction is:",out)
elif choice==3:
    out=num1*num2
    print("output for multiplication is:",out)
elif choice ==4:
    out=num1/num2
    print("output for division is:",out)
else:
    print("invalid choice")