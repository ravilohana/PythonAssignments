# Check if two lists are identical.

list_1 = [3, 11, 7, 9, 5, 6]
list_2 = [5, 11, 9, 7, 3, 4]

list_1.sort()
list_2.sort()

if list_1 == list_2:
    print("lists are identical")
else:
    print("lists are not identical")
