# # 2. Faulty calculator : Give all right results as per user input expect for 2*5 = 80, 5/7 = 1, 8+2 = 20, 1-1 = 11
#
# c = input("Which operation do you want to perform +, *, /, - : ")
# #operator = input()
# a = int(input("Enter the first value: "))
# b = int(input("Enter the Second value: "))
# if a ==2 and b ==5 and c == "*":
#     print("Your result is: ", 80)
# elif c == "*":
#     print(a*b)
# if a ==1 and b ==1 and c == "-":
#     print("Your result is: ", 11)
# elif c == "-":
#     print(a-b)
# if a ==8 and b ==2 and c == "+":
#     print("Your result is: ", 20)
# elif c == "+":
#     print(a+b)
# if a ==5 and b ==7 and c == "/":
#     print("Your result is: ", 1)
# elif c == "/":
#     print(a/b)

# 3. Guess the hidden number : Get user input and inform user if he is close or far from the hidden number. Only 5 chances

# HN = 65
# x = 5
# while x > 0:
#     i = int(input("Guess the hidden Number : "))
#     if i == HN:
#         print("Great you have won the game")
#         break
#     elif i > 65 < 75:
#         print("You are close to the number")
#         x = x-1
#         print("Chances left :", x)
#         continue
#     elif i < 65 > 60:
#         print("You are too far from the number, Number of chances left : ")
#         x = x-1
#         print("Chance left :",x)
#         continue
#     else:
#         print ("Game OVer!! You have used all your chances")
#         break

# 4. Pattern Printing

# I1 = int(input("How many rows do you want= "))
# I2 = bool(int(input("Type 1 or 0= ")))
# #I3 = bool(I2)
# if I2 is True:
#     #i = I1
#     for i in range(1, I1+1):
#         #print(i)
#         print("*"*i)
#
# if I2 is False:
#     #i = I1
#     for i in range(I1, 0, -1):
#         #print(i)
#         print("*" *i)
#         #i - 1
#         #print("*")


#5. Health Management System
# Total 6 Files, 3 For exercise and 3 For for diet
# 3 clients - Harry, Rohan and Hammad
# write a function that when executed takes as input client name
# one more function to retrieve exercise or food for any client

# import datetime
# import time
#
#
# def getdate():
#     return datetime.datetime.now()
#
#
# #clientsname = {1: "Harry", 2: "Rohan", 3: "Hamad"}
#
#
# def log(n):
#     """This is a function for harry"""
#
#     if n == 1:
#         with open("Harry.txt","a") as f:
#             f.write("\n" "Chart for Harry opened at [" + str(getdate())+"]")
#             # f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
#             #print("Success")
#             print(f)
#
#
# # def exercise():
# #     """This is a function for the exercise"""
# #     with open("exercise","a") as op:
# #         return op
#
#
# n = int(input("Input the user number: 1. Harry\n 2. Rohan\n 3. Hamad "))
# # for key,value in clientsname.items():
# #     print("client is :", clientsname[a])
# b = int(input("Do you want to log or open 1.Log or 2.Retrieve "))
# c = int(input("Which option 1. Exercise 2.Diet "))
# print("Successfully updated", log(n))
# print("Time consumed",time.process_time())


# with open("Harry.txt","w") as f:
#     f.write("Test successful, very good")
#
#
# time = str(getdate())
# print(time)
#print(clientname().__doc__)
#
# str(clientname("Harry" + "Good Morning"))
# print(type(clientname()))

#6. Game dev : Snake,water or gun
import random
import string
import time

print("Welcome to Snake Water Gun game!!")
W = 0
L = 0
D = 0
chance = 1
a = str(input("Enter your choice\nS for Snake\nW for Water\nG for Gun\n"))
# rnd = random.choice(["snake","water","gun"])
# if a == str(s):
# rnd = random.choice(["snake", "water", "gun"])
#for i in range(5):

#for chance in range(5):
# if a and rnd == 's':
while chance < 5:

    rnd = random.choice(["snake", "water", "gun"])
    if a == 's' and rnd == 'snake':
        print('Computer selected choice is: ', rnd, "& It's a tie")
        D = D+1
        #chance = chance - 1
        print("The result is :", 'Won :', W, "Lost :", L, "Draw :", D)
        #chance += 1
        print("Chances Remaining :", 5-chance)
        a = str(input("Enter your choice\nS for Snake\nW for Water\nG for Gun\n"))
        #continue

# print("Computer selected choice is :", rnd)
# print("You have lost,Chances left :", i-1)
# continue
    elif a == 's' and rnd == 'water':
    # while chance < 5:   # for i in range(5, 0, 1):
        print("Computer selected choice is :", rnd)
        print("You have won,: ", "Chances used : ",)
        W = W + 1
        print("The result is :", 'Won :', W, "Lost :", L, "Draw :", D)
        #chance += 1
        print("Chances Remaining :", 5-chance)
        #print(chance)
        a = str(input("Enter your choice\nS for Snake\nW for Water\nG for Gun\n"))
        #continue

    elif a == 's' and rnd == 'gun':
    # while chance < 5:   # for i in range(5, 0, 1):
        print("Computer selected choice is :", rnd)
        #chance += 1
        print("You have lost,Chances left :", 5-chance)
        L = L + 1
        print("The result is :", 'Won :', W, "Lost :", L, "Draw :", D)
        a = str(input("Enter your choice\nS for Snake\nW for Water\nG for Gun\n"))
        #continue

    elif a == 'w' and rnd == 'snake':
    # while chance < 5:   # for i in range(5, 0, 1):
        print("Computer selected choice is :", rnd)
        print("You have won")
        W = W + 1
        print("The result is :", 'Won :', W, "Lost :", L, "Draw :", D)
    else:
        print("Invalid entry.Try again",'Chances left :', 5-chance)
        a = str(input("Enter your choice\nS for Snake\nW for Water\nG for Gun\n"))
    #print("chance remaining :", 5-chance)
    chance += 1
if chance == 5:
    if W > L:
        print("You won")
    elif D > W:
        print("Game Draw")
    elif L > W:
        print("Computer won")

print("Game Over!! Used all Chances")
print("The Process time taken is :", time.process_time())
exit()

#chance = chance + 1



# print("You have lost,Chances left :", i)
#     if i == 0:
#         print("No more chances.Game over!!")
# exit()

# rnd = random.choice(["snake", "water", "gun"])
# print("Computer selected choice is :",rnd)
#print("The Process time taken is :", time.process_time())
# exit()
