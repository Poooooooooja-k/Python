# sets are unordered collections.they are unchangable .sets donot contain duplicate values
s={2,4,2,6}
print(s)

imfo={"carla",12,False,5.9}
print(imfo)

harry=set()
print(type(harry))


# set methods
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

cities1={"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities1.intersection(cities2)
print(cities3)
# symmetric difference :prints items that are not similar to both the sets
cities=cities1.symmetric_difference(cities2)
print(cities)
#difference and difference update :only items that are only present in the original set not in both the sets
c=cities1.difference(cities2)
print(c)

# isdisjoint:checks if items in given set is present in another set
d=cities1.isdisjoint(cities2)
print(d)
# issuperset():methods checks if all the items of a particular set is prsent in the original set
s=cities1.issuperset(cities2)
print(s)
# issubset():checks if all the items of the original list are present in the particular set.it returns true if all the items are present,else it returns false
m=cities1.issubset(cities)
print(m)

# add
cities.add("helsinkki")
print(cities)

# remove/discard
cities1.remove("tokyo")
print(cities)
# the main differenec between remove and discard is that if you try to remove an item which is not present in the set.remove raises and error ,but discard doesnot raise any error 
 

# pop
out=["hello","hi","hey"]
item=out.pop()
print(item)
print(out)

# delete():to delete the entire set
# clear():clears all the items of the set and prints an empty set
out.clear()
print(out)