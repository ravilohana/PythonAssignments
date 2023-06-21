# How to check if a list is empty in Python. (if len(lis1) == 0:)

my_list = []


# approach 1
def check_empty_list(given_list):
    if len(given_list) == 0:
        return True
    else:
        return False


print(check_empty_list(my_list))

# approach 2
print(len(my_list) == 0)
