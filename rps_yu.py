#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 21:28:35 2018

@author: YvaineYUU
"""

#Rock Paper Scissors
print("Made by YvaineYuu")
lose = ("The computer WINS!!")
win = ("You WIN!!")
lives = 5
score = 0
drew = 0
computer_lives = 7
print("----------------------------------------------------------------------")
print("Live Rules")
print("You start with",lives,"lives")
print("If your win, you get a certain live.")
print("If you lose, you lose a life")
print("If you drew, the lives stay the same")
print("--------------------------------------")
print("MAKE SURE YOU DON'T USE CAPITALS")
print("---------------------------------------")
print("To see the list of rules, types rules")
print("----------------------------------------")
print("At any point type exit to leave the game")
print("-----------------------------------------")
print("The computer has lives as well. So you better be watch out")
print("Can you BEAT the computer?")
print("May the forth be with you!")
print("------------------------------------------")
while True:
        rps = input("Rock, Paper, Scissors?     ")
        import random
        computer = ("rock","paper","scissors")
        computer = random.choice(computer)
        #rock if statements:
        if rps == "rock" and computer == "paper":
            print("The computer choose",computer)
            print("")
            print(lose)
            print("")
            print("")
            lives-=1
        if rps == "rock" and computer == "scissors":
            print("The computer choose",computer)
            print("")
            print(win)
            print("")
            print("")
            score += 1
        #paper if statements:
        if rps == "paper" and computer == "rock":
            print("The computer choose",computer)
            print("")
            print(win)
            computer_lives -= 1
            print("")
            print("")
            lives += 1
        if rps == "paper" and computer == "scissors":
            print("The computer choose",computer)
            print("")
            print(lose)
            print("")
            print("")
            lives-=1
        #scissors if statments:
        if rps == "scissors" and computer == "paper":
            print("The computer choose",computer)
            print("")
            print(win)
            computer_lives -= 1
            print("")
            print("")
            lives += 1
        if rps == "scissors" and computer == "rock":
            print("The computer choose",computer)
            print("")
            print(lose)
            print("")
            print("")
            lives-=1
        #duplicates:
        if rps == "rock" and computer == "rock":
            print("The computer choose",computer)
            print("")
            print("You Drew")
            print("")
            print("")
            drew += 1
        if rps == "paper" and computer == "paper":
            print("The computer choose",computer)
            print("")
            print("You Drew")
            print("")
            print("")
            drew += 1
        if rps == "scissors" and computer == "scissors":
            print("The computer choose",computer)
            print("")
            print("You Drew")
            print("")
            print("")
            drew += 1
        #system:
        if rps == "rules":
            print("--------------------------------")
            print("RULES")
            print("--------------------------------")
            print("> Rock loses against Paper")
            print("> Rock beats Scissors")
            print("> Paper beats Rock")
            print("> Paper loses against Scissors")
            print("> Scissors beats Paper")
            print("> Scissors loses against Rock")
            print("--------------------------------")
        if rps == "Display Lives":
            print(lives)
        if rps == "Display Score":
            print(score)
        if rps == "Display Drew":
            print(drew)
        #lives
        if lives == 0 or rps == "test":
            print("Thank you for playing the game")
            print("You have run out of lives")
            print("You got",score,"correct")
            print("Yor drew",drew,"times")
            stop = input("Press enter to exist.")
            import time
            time.sleep(900)
        if computer_lives == 0:
            print("Thanks for playing")
            print("The computer losts all its lives. You WIN!!")
            print("You got",score,"correct")
            print("Yor drew",drew,"times")
            stop = input("Press enter to exist.")
            import time
            time.sleep(900)
        #Exit:
        if rps == "exit":
            break
        
                
        
                
                
            
            