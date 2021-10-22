print(0.2+0.3==0.5)
print(0.2+0.1==0.3)
mypi="3.14"
print(type(mypi))
print(float(mypi)*2) # умножение
print(mypi*2) # повторение
# print(mypi+2) # err
print(float(mypi)+2) # add

print(mypi+str(2)) # concatenation


li1=[1,"2",True]
li1[1]="abc"
print(li1, type(li1))

tu1= tuple(li1)
print(tu1,type(tu1))
# tu1[1]="abc"  ## tuple immutable 
# set (mutable)
set_a={1,2,3,4,5}
set_b={3,4,5,6,7}

print(set_a|set_b )
print(set_a&set_b )

# dictionary (mutable)

d_exam_mark=dict(неуд=2, удовл=3, хор=4, отл=5)

print(d_exam_mark["хор"])


