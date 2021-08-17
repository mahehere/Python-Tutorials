#6. Game dev : Snake,water or gun - My 1st self made program :)
import random
import time
import emoji
print("Welcome to Snake Water Gun game!!")
W = 0
L = 0
D = 0
print(emoji.emojize(':snake:'))
chance = 1
a = str(input("Enter your choice\nS for Snake\nW for Water\nG for Gun\n"))
while chance < 5:
    rnd = random.choice(["snake", "water", "gun"])
    if a == 's' and rnd == 'snake':
        print('Computer selected choice is: ', rnd, "& It's a tie")
        D = D+1
        print("The result is :", 'Won :', W, "Lost :", L, "Draw :", D)
        print("Chances Remaining :", 5-chance)
        a = str(input("Enter your choice\nS for Snake\nW for Water\nG for Gun\n"))
    elif a == 's' and rnd == 'water':
        print("Computer selected choice is :", rnd)
        print("You have won,: ", "Chances used : ",)
        W = W + 1
        print("The result is :", 'Won :', W, "Lost :", L, "Draw :", D)
        print("Chances Remaining :", 5-chance)
        a = str(input("Enter your choice\nS for Snake\nW for Water\nG for Gun\n"))

    elif a == 's' and rnd == 'gun':
        print("Computer selected choice is :", rnd)
        print("You have lost,Chances left :", 5-chance)
        L = L + 1
        print("The result is :", 'Won :', W, "Lost :", L, "Draw :", D)
        a = str(input("Enter your choice\nS for Snake\nW for Water\nG for Gun\n"))

    elif a == 'w' and rnd == 'water':
        print("Computer selected choice is: ", rnd, "&It's a tie")
        W = W + 1
        print("The result is :", 'Won :', W, "Lost :", L, "Draw :", D)
    else:
        print("Invalid entry.Try again", 'Chances left :', 5-chance)
        a = str(input("Enter your choice\nS for Snake\nW for Water\nG for Gun\n"))
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
