# Numbers in a list within a given range.

# Input : [10, 20, 30, 40, 50, 40, 40, 60, 70] range: 40-80
# Output : 6

my_list = [10, 20, 30, 40, 50, 40, 40, 60, 70, 15, 36, 90, 55, 88]
counter = 0
left = 10
right = 40
for i in my_list:
    if left <= i <= right:
        counter = counter + 1
print(counter)

my_list_1 = [1, 2, 3, 4, 10, 2]
print(sum(my_list_1))
