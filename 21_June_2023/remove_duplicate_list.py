# Remove duplicates from list.

#
# my_list = [9, 7, 11, 3, 9, 11, 7, 15, 9]
# print("Unsorted list: ", my_list)
# sorted_list = sorted(my_list)
# print("Sorted List : ", sorted_list)
#
# for i in range(len(sorted_list)):
#     if sorted_list[i] == sorted_list[i+1]:
#         sorted_list.remove(sorted_list[i])
#         print(sorted_list)


my_list = [9, 7, 11, 3, 9, 11, 7, 15, 9, 17, 3, 21, 11, 33, 3, 7, "ABC", "abc", "ABC", True, False, True, 14.5, 14.05,
           169.1258, 16.14]
print("Original List Before removing duplicate : ", my_list)

'''
res = []
# print(type(res))
for i in range(len(my_list)):
    # index() function will fetch the first occurrence of an element
    if i == my_list.index(my_list[i]):
        res.append(my_list[i])
        # print(type(res))
        # print(res)

print("Original List After removing duplicate : ", res)

'''
'''
res = []
for i in my_list:
    if i not in res:
        res.append(i)

print("Original List After removing duplicate : ", res)
'''


def remove_duplicate_list(list_params):
    res = []
    for i in my_list:
        if i not in res:
            res.append(i)
    return res


def remove_duplicate_list_1(list_params):
    res = []
    for i in range(len(my_list)):
        # index() function will fetch the first occurrence of an element
        if i == my_list.index(my_list[i]):
            res.append(my_list[i])
            # print(type(res))
            # print(res)
    return res


print("Original List After removing duplicate remove_duplicate_list(list_params) : ", remove_duplicate_list(my_list))
print("Original List After removing duplicate remove_duplicate_list_1(list_params) : ",
      remove_duplicate_list_1(my_list))
