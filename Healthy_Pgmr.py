# 7.Healthy Programmer

""" There should a reminder for the below exercise in the specified intervals
Work Duration 9-5pm
1. water -  water.mp3 - 3.5l water - input drank - timestamp log
2. eyes - eyes.mp3 - done - run every 30 minutes
3. phys activity - phy.mp3 - every 45 minutes
Rules
use pygame module"""

import pygame  # For playing the mp3 file
import datetime  # Module for getting the system time in log
import time  # Module to get set the sleep time for constant reminder


print("This is a Healthy Programmer S/W")
print("The Work duration is from 9AM to 5PM")


def getdate():
    """This function is for getting the current system date and log it in txt file"""
    return datetime.datetime.now()


def water():
    """This is the water function to remind programmer about drinking water"""

    pygame.mixer.init()
    pygame.mixer.music.load("Drinking-Water.mp3")
    pygame.mixer.music.play(-1)
    a = input(str("Please type 'done' after drinking 1 cup water: ")).capitalize()
    while True:
        if a != "Done":
            pygame.mixer.music.play(-1)
            a = input("Please type 'done' after drinking 1 cup water: ").capitalize()  # Getting user input and
            # capitalising first char
        elif a == "Done":
            pygame.mixer.music.stop()
            print("Next Reminder is after 30 Minutes")
            f = open("Water.txt", "a")  # can also use file command using "with open("Harry.txt","w") as f:"
            f.write("Last water intake for Programmer was at " + str(getdate()) + "")  # calls and logs the time in txt file
            f.write(" & The user input is: " + a + "\n")
            f.close()  # close the txt file
            break


def eyes():
    print("This is the Eye function")
    f = open("Eyes.csv", "a")
    print(datetime.datetime.now())
    f.close()


def phy_exercise():
    print("This is the Exercise function")
    f = open("Physical Exercise.csv", "a")
    print(datetime.datetime.now())
    f.close()


time.sleep(5)
water()
