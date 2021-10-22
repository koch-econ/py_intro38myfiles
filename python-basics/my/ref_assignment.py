list1=[1,2]
list2=list1
list3=list(list1)
list2[0]=-1
print(id(list1))
print(id(list2))
print(id(list3))
print(list1)
print(list3)

