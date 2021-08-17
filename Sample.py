# # Health Management System
#
# client_list = {1: "Harry", 2: "Rohan", 3: "Hammad"}
#
# lock_list = {1: "Exercise", 2: "Diet"}
#
#
# def getdate():
#
#     import datetime
#
#     return datetime.datetime.now()
#
#
# try:
#
#     print("Select Client Name:")
#
#     for key, value in client_list.items():
#
#         print("Press", key, "for", value, "\n", end="")
#
#     client_name = int(input())
#
#     print("Selected Client : ", client_list[client_name], "\n", end="")
#
#     print("Press 1 for Lock")
#
#     print("Press 2 for Retrieve")
#
#     op = int(input())
#
#     if op == 1:
#
#         for key, value in lock_list.items():
#
#             print("Press", key, "to lock", value, "\n", end="")
#
#         lock_name = int(input())
#
#         print("Selected Job : ", lock_list[lock_name])
#
#         f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "a")
#
#         k = 'y'
#
#         while k != "n":
#
#             print("Enter", lock_list[lock_name], "\n", end="")
#
#             mytext = input()
#
#             f.write("[ " + str(getdate()) + " ] : " + mytext + "\n")
#
#             k = input("ADD MORE ? y/n:")
#
#             continue
#
#         f.close()
#
#     elif op == 2:
#
#         for key, value in lock_list.items():
#
#             print("Press", key, "to retrieve", value, "\n", end="")
#
#         lock_name = int(input())
#
#         print(client_list[client_name], "-", lock_list[lock_name], "Report :", "\n", end="")
#
#         f = open(client_list[client_name] + "_" + lock_list[lock_name] + ".txt", "rt")
#
#         contents = f.readlines()
#
#         for line in contents:
#
#             print(line, end="")
#
#         f.close()
#
#     else:
#
#         print("Invalid Input !!!")
#
# except Exception as e:
#
#     print("Wrong Input !!!",e)
#
# import pyperclip
# a = pyperclip.copy("copy this")
# b = pyperclip.paste()
# print(b)
#
# from emoji import emojize
# print(emojize("There is a :snake: in his pocket, :thumbs_up:"))
#
# howdoi save in pyperclip


import random
print("The game will be total of 10 rounds\nPress: 's' for Snake or 'w' for Water or 'g' for Gun")
i=0
win=0
lost=0
draw=0
while i<10:
    lst=["Snake", "Water", "Gun"]
    choice=random.choice(lst)
    n=input("\nEnter your choice: ")
    if choice=="Snake":
        if n=="s":
            print("Computer's choice: ",choice,"\nRound Draw!!!")
            draw+=1
        elif n=="w":
            print("Computer's choice:",choice,"\nYou have won this round!!!")
            win+=1
        elif n=="g":
            print("Computer's choice:",choice,"\nYou have lost this round!!!")
            lost+=1
        else:
            print("You have entered a wrong choice")
    elif choice=="Water":
        if n=="w":
            print("Computer's choice:",choice,"\nRound Draw!!!")
            draw+=1
        elif n=="g":
            print("Computer's choice:",choice,"\nYou have won this round!!!")
            win+=1
        elif n=="s":
            print("Computer's choice:",choice,"\nYou have lost this round!!!")
            lost+=1
        else:
            print("You have entered a wrong choice")
    else:
        if n=="g":
            print("Computer's choice:",choice,"\nRound Draw!!!")
            draw+=1
        elif n=="s":
            print("Computer's choice:",choice,"\nYou have won this round!!!")
            win+=1
        elif n=="w":
            print("Computer's choice:",choice,"\nYou have lost this round!!!")
            lost+=1
        else:
            print("You have entered a wrong choice")
    print("Left-over round number: ",10-i)
    a=f"\nTill now the score is:\nYou: {win}\nComputer: {lost}\nDraw: {draw}"
    print(a)
    i+=1
if i==10:
    if win>lost:
        print("\nWinner!!! You have won the game")
    elif lost>win:
        print("\nGame Over!!! You have lost the game")
    else:
        print("\nGame Draw!!!")



