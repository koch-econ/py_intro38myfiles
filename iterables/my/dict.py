#%%
lname='Kochergin'
print(hash(lname))
# %%
256**80
# %%
N=10
def myhash (p):
    return hash(p)%N
# %%
myhash(lname)
# %%
lname='Denisov'
myhash(lname)
# %%

lname='Kot'
myhash(lname)
# %%
hash(tuple(range(2)))
# %%
hash(list(range(2)))
# %%
rus_eng={"плохой":"bad","кот":"cat"}
for w in rus_eng:
    print(w)
# %%
for w in rus_eng.keys():
    print(w)

# %%
for w in rus_eng.items():
    print(w)

# %%
# %%
for rus, eng in rus_eng.items():
    print(rus,"по-английски",eng)

# %%
s1={1,2,5}
s2={4,5,6}
print(s1.union(s2))
print(s1|s2)
print(s1.intersection(s2))
print(s1&s2)
#%%
5 in s1
# %%
"плохой" in rus_eng
# %%
def add_to_dict(**new_rus_eng):
    rus_eng.update(new_rus_eng)
# %%
add_to_dict(хороший="good",милый="nice")

rus_eng
# %%
