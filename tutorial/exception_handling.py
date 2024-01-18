
# exception handling is the process of responding to unwanted or unexpected events when a computer program runs
# a=input("enter the number: ")
# print(f"multiplication table of {a} is: ")
# try:
#     for i in range(1,11):
#         print(f"{int(a)}x{i}={int(a)*i}")
# except:
#     print("invalid input")



# try:
#     num=int(input("enter an integer: "))
# except ValueError:
#     print("number entered is not an integer")
# except IndexError:
#     print("index error")

# finally:also part of exception handling.this block is always executed
# try:
#     l=[1,5,6,7]
#     i=int(input("enter the index"))
#     print(l[i])
# except:
#     print("some error occured")
# finally:
#     print("i am always exceuted")


# customerror:we can raise custom error by uisng the raise keyword
a=int(input("enter any value between 5 and 9: "))
if (a<5 or a>9):
    raise ValueError("value should be between 5 ans 9")
