# import os
# print(os.getcwd())

# Open my-file.txt and assign result to f.
with  open("python-basics/Demos/my-file.txt") as f:
    # Read contents of file into content variable
    content = f.read() 
    # Close the file.
print(content) # Print content.