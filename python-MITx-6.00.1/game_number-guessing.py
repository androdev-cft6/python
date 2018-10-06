# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
num_guess=0
num_low=0
num_high=100

str_response=""
str_guess="Is your secret number " + str(num_guess) + "?"
str_prompt= "Enter 'h' to indicate the guess is too high. "\
            "Enter 'l' to indicate the guess is too low. "\
            "Enter 'c' to indicate I guessed correctly ==> "
str_wrong_input="Sorry I didn't understand your input"
str_game_over="Game over. Your secret number was: "


input("Please think of a number between 0 and 100, press 'Enter' when ready ")
while str_response!="c":
    num_guess=(num_high+num_low)//2
    print("Is your secret number", num_guess, end='?')
    str_response=input(str_prompt)
    if str_response=='l':
        num_low=num_guess    
    elif str_response=='h':
        num_high=num_guess
    elif str_response=='c':
        print("Game over. Your secret number was", num_guess, end='.')
        break
    