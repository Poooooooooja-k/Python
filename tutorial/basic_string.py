name="pooja"
friend="vaishnavi"
another_friend="anjali"
print("hello,"+name)
apple='he said,"I want to eat an apple"'
print(apple)
new='''hi pooja
i want an apple
can you buy me one?'''
print(new)
# when you have multiple lines of code if "" is used error might occur
# so use ''' ''' or """ """
string="poooja"
print(string[0])
# accessing characters in a string
# 1st aplhabet will be returned
for i in string:
    print(i)
    # looping through the characters of the string using for loop

# slicing in string
# for slicing use []brackets
names="pineapple"
print(names[0:2])
# print the alphabets from start to 2 alphabets
print(names[:4])
print(names[:])
print(names[0:-3])
print(names[-3:-1])
# removes last 3 alphabets 
len1=len(names)
print("pineapple is a",len1,"letter word")
# returns the length of the string