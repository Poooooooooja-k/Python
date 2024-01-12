# dictionary is an ordered collection of data items .they have key-value pair
dic={
    344:"harry",
    56:"pooja",
    89:"sumi",
    567:"sneha"
}
# print(dic[567] )
# print(dic.keys())
# print(dic.values()).
# print(dic.items())

# update 
ep1={122:45,123:89,567:69,670:69}
ep2={222:67,565:90}
ep1.update(ep2)
print(ep1)
# clear()method is used to remove all the items from the dictionary
ep1.pop(122)
print(ep1)
# popitem():method removes the last key-value pair from the dictionary
ep2.popitem()
print(ep2)
# del :delete the whole dictionary
