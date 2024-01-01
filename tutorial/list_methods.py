l=[1,5,2,3]
print(l)
# insert an element into a list we use append()
l.append(7)
# reverse th list
l.reverse()
print(l)
print(l.index(1))
l.sort(reverse=True)
print(l)
# inserts 899 at position 1
l.insert(1,899)
# copy() method is used to create a copy of the list
m=l.copy()
print("m is",m)
n=[900,1000,1100]
k=l+n 
print(k)
# adds n at the end of l
l.extend(n)
print(l)