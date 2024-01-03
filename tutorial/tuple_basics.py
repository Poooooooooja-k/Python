# tuples are unchangable .ordered collection  
tup=(1,5,6,"green","yellow.8")
print(tup[0])
# can do +ve and -ve indexing
if 5 in tup:
    print("yes present")
# indexing
tup2=tup[1:3]
print(tup2)

# tuple methods
#  tuples are immutable .hence if you want to add ,remove or change anything 1st you need to convert tuple to list
countries=("spain","italy","india","england")
temp=list(countries)
temp.append("russia")
temp.pop(3)
# change items
temp[2]="finland"
print(countries)

# count()method
tuple1=(0,1,2,3,2,3,1,3,2,3,2,1)
res=tuple1.count(3)
print("count of 3 in tuple1 is:",res)
# tuple.index(element,start,end)
nes=tuple1.index(3,4,8)
print("count of 3 in tuple1 is:",nes)