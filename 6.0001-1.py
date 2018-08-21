# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#%%
import random as rd
print(rd.randint(1,100))


#%%
num = input("G.S says something to me: ")
print(num*100)

#%%
input_1 = float(input("enter a number: "))
input_2 = float(input("enter a number: "))
if input_1 == input_2:
    print("input_1 is equal to input_2")
    if input_1 == 0:
        print("input_1*input_2",0)
    if input_1 != 0:
        print("input_1/input_2", input_1/input_2)
elif input_1 < input_2:
    print("input_1 is smaller")
elif input_1 > input_2:
    print("input_1 is greater than input_2")
    
#%%
for i in range(10):
    print("I love you, Qiwen Yu", "!!!")
    
#%%
#practice for guess&check algorithem
cube = float(input("enter a number:"))
for guess in range(int(abs(cube))+1):
    if guess**3 >= abs(cube):
        break
if guess**3 != abs(cube):
    print("The cube is not the perfect cube")
    print("The close guess is "+str(guess))
else:
    if cube < 0:
        guess = -guess
    print("Cube root of "+str(cube)+" is "+str(guess))
    
#%%
#practice for approxiation solution
cube = float(input("enter a number:"))
epsilon = 0.001
increment = 0.0000001
guess = 0.000
num_guesses = 0
while abs(guess**3-cube) >= epsilon:
    guess += increment
    num_guesses += 1
print("The number of guesses is ", num_guesses)
if abs(guess**3-cube) >= epsilon:
    print("There is no suitable guess for ", cube)
else:
    print("The closest value for cube is", guess)

68.7

#%%
#bisecton practice
cube = float(input("ENTER A NUMBER:"))
low = 0
high = cube
guess = (high+low)/2.0
num_guesses = 0
epsilon = 0.00001
while abs(guess**3-cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    num_guesses += 1
    guess = (high+low)/2.0
print("It takes ", num_guesses,"times to get the cubic root ",guess,"for", cube)


