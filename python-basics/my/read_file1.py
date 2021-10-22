import os
print(os.getcwd())

f = open("python-basics/Demos/my-file.txt") # Open my-file.txt and assign result to f.
content = f.read() # Read contents of file into content variable.
print(content) # Print content.
f.close() # Close the file.