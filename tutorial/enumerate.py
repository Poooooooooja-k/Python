# enumerate:allows you to loop over a sequence(list,tuple,string)and get the index and value of ecah element in the sequence at the same time  
# marks=[12,56,32,98,12,45,1,4]
# for index,mark in enumerate(marks):
#     print(mark)
#     if index==3:
#         print("awesome")

fruits=['apple','banana','mango','pineapple','strawberry']
for index,fruit in enumerate(fruits,start=0):
    print(index,fruit)
# can set a start value also like "start="