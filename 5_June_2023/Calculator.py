# Create Calculator
# Take a input from a user - a,b
# a+b, a-b,a*b,a/b

a = input("Enter the value of a ")
b = input("Enter the value of b ")

operators = input("Enter the operator")

# if a == "":
#     # print("Please enter the value of a")
#     a=int(0)
# elif b == "":
#     # print("Please enter the value of b")
#     b=int(0)

# if a == '' or b == '':
#     print("PLease don't enter the emplty value!")


if(int(a) == 0):
    print("PLease don't enter the emplty value!")
elif(int(b) == 0):
    print("PLease don't enter the emplty value!")



sum = int(a) + int(b)
diff = int(a) - int(b)
mul = int(a) * int(b)
div = int(a) / int(b)

# sum = int(float(a)) + int(float(b))
# diff = int(float(a)) + int(float(b))
# mul = int(float(a)) + int(float(b))
# div = int(float(a)) + int(float(b))



if operators == "+":
    print("The Sum of a and b " , sum)
elif operators == "-":
    print("The Difference of a  and b ",diff)
elif operators == "*":
    print("The Multiplication of a and b",mul)
elif operators == "/":
    
    print("The division of a and b ", div)
else:
    print("Please enter the correct values of a,b and operators")




