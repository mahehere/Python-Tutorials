# Day 1 - strings, variable, len, print,input
print("Hello world!\n"'Mahesh'+' M')
print("Day 1 - Python Print Function")
print("Day 1 - String manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "World")')
print("New lines can be created with a backslash and n.")
print("Hi " + input("What is your name? ") + " Nair")
print("Hi" + input("Please enter your name"))
# print("The length of your name is :", len(a))
print("The length of you name is:", + len(input("What is your Name: ")))
a = input("Your name")
print(a)
numb1 = int(input("a: "))
num2 = int(input("b: "))
c = num2
num2 = numb1
print("a: ", c)
print("b", num2)
time_until = "5"
print("entered" + time_until + "values")
# Program to get input and display the combined result
print("Welcome to the band name generator program\n")
city = input("What city did you grow up in\n")
pet_name = input("What is the name of your pet\n")
print("The name of your Band can be :" + city + pet_name)

# Day 2 - data types, numbers, operations, type conversion, f-strings

print("Hello"[4])

a = input("enter a 2 digit number: ")
# print(a[0])
b = int(a[0]) + int(a[1])
print(b)

print((3*3) / 3 + 3 - 3)

# Ex 1: BMI calculator

Height = input("Enter height in Mts: ")
Weight = input("Enter weight in Kgs: ")
a = (float(Height) ** 2)
b = int(Weight) / a
print(b)
print(int(b))
print(round(b, 3))

# Ex 2: Life in weeks

age = input("Type in your age: ")
days = 365
weeks = 52
months = 12
max_age = 90
actual_age = int(max_age) - int(age)
w = weeks * actual_age
m = months * actual_age
print(f"You have {actual_age * 365} days, {w} weeks and {m} months left.")

# Ex 3:Tip calculator

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

# Day 3 - Cond. statements, logical operators, code blocks and scope

print("Welcome to Even or number guess game")
user_num = int(input("Please enter you number to check: "))
if user_num % 2 == 0:
    print("Your number is Even")
else:
    print("Your number is odd")

# Ex 4: BMI calculator 2.0

print("Calculate you BMI")
Height = input("Enter height in Mts: ")
Weight = input("Enter weight in Kgs: ")
a = float(Height) ** 2
b = float(Weight) / a
rnd = round(b)
if b <= 18.5:
    print(f"Your BMI is {rnd} and You are underweight")
elif b < 25:
    print(f"BMI is {rnd}.You are normal weight")
elif b < 30:
    print(f"BMI is {rnd}.You are overweight")
elif b < 35:
    print(f"BMI is {rnd}.You are obese")
else:
    print(f"BMI is {rnd}.You are clinically obese")

# Ex5: To check leap year

print("Lets find if the year is a leap or not!!")
user_input = int(input("Enter the year: "))
a = user_input % 4
b = user_input % 100
c = user_input % 400
if a + b == 0:
    if a + b + c == 0:
        print(f"The year {user_input} is a leap year")
else:
    print(f"The year {user_input} is not a leap year")

# Ex 6: Pizza delivery

print("Welcome to Noombal pizza shop")
size = input("What size pizza do you want: S,M or L: ")
add_on = input("Do you want Pepperoni added: 'Y' or 'N': ")
cheese = input("Do you want extra cheese: 'Y' or 'N': ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
if add_on == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
if cheese == "Y":
    bill += 1
print(f"The total bill is: {bill}")

# Ex 7: Roller coaster ticket vending

print("Welcome to roller coaster ticket vending machine!")
height = int(input("Enter you height: "))
age = int(input("Please enter your age: "))
bill = 0
if height <= 120:
    print("Sorry.. You cant ride on roller coaster as your height should be more than 120 cm")
if height > 120:
    if age <= 12:
        bill += 5
    elif age <= 18:
        bill += 7
    elif age >= 45 <= 55:
        print(f"You are eligible for free ticket, Bill cost: {bill}")
    else:
        bill += 12
    photo = input("Do you want photo. Y or N: ")
    if photo == "Y":
        bill += 3
    print(f"Final bill amount: {bill}")

# Ex 8: Love Calculator

print("Welcome to the Love Calculator!!")
name1 = str(input("Enter the 1st person name: "))
name2 = input("Enter the 2nd person name: ")
change_case = name1.lower()
change = name2.lower()
full_name = change_case + change
count1 = full_name.count("t")
count2 = full_name.count("r")
count3 = full_name.count("u")
count4 = full_name.count("e")
count5 = full_name.count("l")
count6 = full_name.count("o")
count7 = full_name.count("v")
count8 = full_name.count("e")
print("T: ", count1)
print("R: ", count2)
print("U: ", count3)
print("E: ", count4)
print("L: ", count5)
print("O: ", count6)
print("V: ", count7)
print("E: ", count8)
total = count1 + count2 + count3 + count4
total1 = count4 + count5 + count6 + count7
grand_score = str(total) + str(total1)
if int(grand_score) < 10 or int(grand_score) > 90:
    print(f"your score is {int(grand_score)}, coke and mentos")
elif (int(grand_score) >= 40) and (int(grand_score) <= 50):
    print(f"Your score is : {int(grand_score)}, alright")
else:
    print(f"Your score is: {int(grand_score)}")
print("Total Chars matching with True: ", total)
print("Total Chars matching with love: ", total1)
print("Final score is:", str(total) + str(total1))

# Ex 9: Treasure Island

print("Welcome to the Treasure Island!!")
user_input = input("Where do you want to go : Left\'s or Right\n")
if user_input == "Left":
    user_input1 = input("What do you want to do: Swim or Wait\n")
    if user_input1 == "Wait":
        user_input2 = input("which door you want to go: Red, Yellow or Blue\n")
        if user_input2 == "Yellow":
            print("You win")
        else:
            print("Game over. You lose")
    else:
        print("Game over. You lose")
else:
    print("Game over. You lose")
