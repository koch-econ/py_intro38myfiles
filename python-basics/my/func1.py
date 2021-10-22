def dist(x1,y1,x2,y2):
    # print("внутри dist")
    d_x = x2-x1
    d_y = y2-y1
    return (d_x**2 + d_y**2)**0.5

point_a=(1,1)
point_b=(-1,2)
point_c=(4,2)
print(point_a, point_b, point_c)
print("a---b:",dist(point_a[0],point_a[1],point_b[0],point_b[1]) )
print("a---c:",dist(point_a[0],point_a[1],point_c[0],point_c[1]) )
print("адрес ф-и: ", dist     )


rastoyanie = dist

print("a---b:",rastoyanie(point_a[0],point_a[1],point_b[0],point_b[1]) )
print("a---c:",rastoyanie(point_a[0],point_a[1],point_c[0],point_c[1]) )



print("abs value: ", abs(-200))


import math

# print(vars(math))

print(math.e,math.pi,"числа е и пи")

print(math.sin(math.pi/6),"sin pi/3")