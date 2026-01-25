# list1 = [1, 3, 4, 9, 8]
# n = len(list1)

# for i in range(n):
#     for j in range(0, n - i - 1):
#         if list1[j] > list1[j + 1]:
#             list1[j], list1[j + 1] = list1[j + 1], list1[j]

# print(list1)





##### Task 1 lol


def bubble_sort(numbers):
    list1 = numbers
    n = len(list1)

    for i in range(n):
        for j in range(0, n - i - 1):
            if list1[j] > list1[j + 1]:
                print("The numbers in the list are not in ascending order")
                break
            else:
                continue
    
    print("The numbers in the list are in ascending order")


    

    

    
    
    
    

a = [1, 3, 4, 8, 14, 17, 32, 41, 44, 45]
b = [6, 13, 15, 17, 18, 34, 41, 40, 44, 46]
c = [18, 22, 23, 26, 27, 34, 36, 37, 44, 47]
d = [3, 7, 8, 16, 45, 31, 20, 22, 14, 23]

bubble_sort(a)
bubble_sort(b)
bubble_sort(c)
bubble_sort(d)














###Task 2



# def bubble_sort(numbers):
    
#     list = [numbers]
#     n = len(list)

#     for i in range(n):
#         for j in range(0, n - i - 1):
#             if list[j] > list[j + 1]:
#                 list[j], list[j + 1] = list[j + 1], list[j]

#     print(list)


# bubble_sort(9, 6, 3, 25, 21, 8, 23, 1, 17, 14)
# bubble_sort(37, 39, 41, 29, 9, 25, 43, 21, 3, 42)
# bubble_sort(24, 8, 10, 22, 45, 34, 28, 39, 3, 32)
# bubble_sort(15, 21, 8, 32, 46, 44, 37, 20, 27, 22)
# bubble_sort(11, 38, 4, 28, 24, 41, 15, 10, 45, 14)




