# lists are ordered collection of data items
# they store multiple data in a single variable 
# lists are changeable we can alter them after creation
marks=[3,5,6,"harry",1,2,8,7,6]
print(marks[0])
print(marks[-3])   
# negative indexing
if 7 in marks:
    print("yes")
else:
    print("no")
# indexing
print(marks[:])
print(marks[1:-1])
print(marks[1:4])
print(marks[1:8:2])
# list comprehension
# list comprehension is used for creating new lists from other iterables like lists,tuples,dictionaries etc
lst=[i for i in range(4)]
print(lst)
lst1=[i*i for i in range(10) if i%2==0]
print(lst1)
name=["hello","sarah","bruno","pooja"]
new=[i for i in name if len(i)>4]
print(new)