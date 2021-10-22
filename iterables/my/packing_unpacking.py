print(range(10),sep=":")
print(*range(10),sep="\n")

v1,v2,v3 = range(3)
print(v1,v2,v3)
v1, *other = range(13)
print(v1,other)
*other,v_end = range(13)
print(other,v_end)

arg1=(2,10)
arg2=(3,2)

print( pow(*arg1))
print( max(*arg1))
print( min(*arg1))

print_opt={"end":"\n===\n", "sep":"; "}

print(*range(1,12),**print_opt)