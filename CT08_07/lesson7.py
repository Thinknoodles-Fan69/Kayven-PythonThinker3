import os

# filepath = os.getcwd()

# fullpath = os.path.join(filepath, "CT08_07/lesson7_guide.md")

# # print(fullpath)


# if os.path.exists(fullpath):
#     print("{} exist".format(fullpath))
# else:
#     print("{} does not exist".format(fullpath))


file = os.open("test.txt", "w")
file.write("testing save")
file.close()

file = open("test.txt", "r")
content = file.read()
print(content)
file.close()