#  fstring=it is a string formatng mechanism.it offers a convenient way to embed python expressions inside string literals for formating
letter="hey my name is {} and i am from {}"
name=input("enter your name: ")
country=input("enter your country: ")
print(letter.format(name,country))

# using fstring
job=input("enter your job: ")
print(f"i am a {job}")

price=int(input("enter the price: "))
print(f"the price is {price}")