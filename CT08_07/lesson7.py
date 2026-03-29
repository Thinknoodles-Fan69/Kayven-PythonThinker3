import os

# filepath = os.getcwd()

# fullpath = os.path.join(filepath, "CT08_07/lesson7_guide.md")

# # print(fullpath)


# if os.path.exists(fullpath):
#     print("{} exist".format(fullpath))
# else:
#     print("{} does not exist".format(fullpath))


# file = open("test.txt", "w")
# file.write("testing save")
# file.close()

# file = open("test.txt", "r")
# content = file.read()
# print(content)
# file.close()


with open('example 1.txt', 'w') as file:
    file.write('Example 1 With')

with open('example 1.txt', 'r') as file:
    contents = file.read()
    print(contents)

with open('example 1.txt', 'a') as file:
    file.write('\nLine 2')


with open('example 1.txt', 'w') as file:
    file.write('Example 1 With')

with open('example 1.txt', 'r') as file:
    contents = file.read()
    print(contents)


with open('example 1.txt', 'w') as file:
    lines = ['\nLine 1', '\nLine 2', '\nLine 3']
    file.writelines(lines)

with open('example 1.txt', 'r') as file:
    contents = file.read()
    print(contents)

with open('example 1.txt', 'r') as file:
    contents = file.readlines()
    for i in contents:
        print(contents)

    