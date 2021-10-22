list1=range(10)
# print(", ".join(list1))
str_list = []
for i in list1:
    str_list.append(str(i))
print(str_list)
print("; ".join(str_list))
print(": ".join(map(str,list1)))