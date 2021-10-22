# import os
# print(os.getcwd())
text ="""
Poem

Odnazhdy v ...
Sizu ...
"""
# Open my-file.txt and assign result to f.
with  open("python-basics/Demos/my-file2.txt","w") as f:
    f.write(text)
    f.write("=="*10)
    print('2+2=',2+2,file=f)
print("файл записан") 