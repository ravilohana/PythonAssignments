# Check for Sub-List in List.

mylist_1 = [3, 7, 5, 11, 9, 13, 17, 15,21]
mylist_2 = [5, 9, 11, 15,21]

isSubList = False
# print(all(i in mylist_1 for i in mylist_2))
if all(i in mylist_1 for i in mylist_2):
    isSubList = True

if isSubList:
    print("yes sublist")
else:
    print("NO sublist")

