#%%
r1 = range(10)
print(r1)
# %%
print(r1[5])

# %%
i1 = iter(r1)
print(next(i1))
print(next(i1))
print(next(i1))
print(next(i1))

# %%
li1 =[1,2,2,-5,56,5]
i1 = iter(li1)
print(next(i1))
print(next(i1))
print(next(i1))
print(next(i1))
# %%
%%writefile lines.txt
111
222
3333
#%%
with open('lines.txt') as i1:
    print(next(i1),end="")
    print(next(i1),end="")
    print(next(i1),end="")
# %%
rr1=reversed(r1)
print(rr1)
# %%
rr1[2]
# %%
print(next(rr1))
print(next(rr1))
print(next(rr1))
print(next(rr1))
#%%
dir(rr1)
# %%
dir(r1)
# %%
for i in rr1:
    print(i) 
# %%
print(next(rr1))

# %%
for i in rr1:
    print(i) 

# %%
tuple(reversed(range(10)))
# %%
tuple("Hello")
# %%
for ch in "Hello!":
    print(ch)
#%%
"Hello"[-1]
# %%
d1=dict()
d1[2]=4
d1[3]=9
d1[0]=0

d1[3]
#%%

mylist=list(range(20,40,2))
print(mylist)
# %%
mylist.append("lala")
mylist.append( () )
print(mylist)
# %%
mylist.append( 22 )
mylist.remove(22)
print(mylist)
# %%
del mylist[2:4]
print(mylist)

# %%
mylist.reverse()
print(mylist)
# %%
mylist.remove( 'lala' )
# mylist.remove( () )
mylist.sort()
print(mylist)
# %%
mylist.sort( reverse=True)
print(mylist)
#%%

stack=[]
stack.append(1324) # push
stack.append(24) # push
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)
# %%
colors = ["red", "blue", "green", "orange"]
colors_copy2=colors
colors_copy=colors.copy()
print(colors==colors_copy)
print(colors==colors_copy2)
# %%
print(colors is colors_copy)
print(colors is colors_copy2)

# %%
