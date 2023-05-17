import os
# a = os.path.join(os.path.expanduser("~"), "Desktop")
# print(a)
# print(os.getcwd())

# current working path
cur_path = os.getcwd()
print(cur_path)
if not os.path.isdir("image"):
    os.makedirs('image')  # make a folder called image
    print("folder created successfully!")
else:
    print("folder existed!")
    pass