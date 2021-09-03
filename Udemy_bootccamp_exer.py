# Day 1 - strings, variable, len, print,input
# print("Hello world!\n"'Mahesh'+' M')
# print("Day 1 - Python Print Function")
# print("Day 1 - String manipulation")
# # print('The function is declared like this')
# # print("print('what to print ')")
# print('String Concatenation is done with the "+" sign.')
# print('e.g. print("Hello " + "World")')
# print("New lines can be created with a backslash and n.")
# print("Hi " + input("What is your name? ") + " Nair")
# print("Hi" + input("Please enter your name"))
# # print("The length of your name is :", len(a))
# print("The length of you name is:", + len(input("What is your Name: ")))
# print(len(input))
# a = input("Your name")
# print(a)
# numb1 = int(input("a: "))
# num2 = int(input("b: "))
# c = num2
# num2 = numb1
# print("a: ", c)
# print("b", num2)
# time_until = "5"
# print("entered"+time_Until+"values")
# Program to get input and display the combined result
# print("Welcome to the band name generator program\n")
# city  =input("What city did you grow up in\n")
# pet_name = input("What is the name of your pet\n")
# print("The name of your Band can be :" + city + pet_name)

# Day 2 - data types, numbers, operations, type conversion, f-strings

# print("Hello"[4])

# a = input("enter a 2 digit number: ")
# # print(a[0])
# b = int(a[0]) + int(a[1])
# print(b)

# print((3*3) / 3 + 3 - 3)

# BMI calculator
# Height = input("Enter height in Mts: ")
# Weight = input("Enter weight in Kgs: ")
#
# a = (float(Height) ** 2) #* float(0.01)
# b = int(Weight) / a
# print(b)
# print(int(b))
# print(round(b, 3))

# Life in weeks

# age = input("Type in your age: ")
# days = 365
# weeks = 52
# months = 12
# max_age = 90
# actual_age = int(max_age) - int(age)
# # d = days * actual_age
# w = weeks * actual_age
# m = months * actual_age
# print(f"You have {actual_age * 365} days, {w} weeks and {m} months left.")

# Tip calculator
print("Welcome to tip calculator")
d = float(input("Total bill: ₹ "))
print("How much tip percentage to add: 12,15,20: ")
e = int(input("Tip percentage: "))
c = int(input("total ppl: "))
a = ((d * e) / 100)
final_amt = d + a
b = "{:.2f}".format(final_amt/c)
# b = round(final_amt/c, 2)
print(f"Each person split is: {b}")

