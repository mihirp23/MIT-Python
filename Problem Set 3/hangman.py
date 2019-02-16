#!/usr/bin/env python

###############################################################################
# Name : Mihir Patel
# Date : 2/16/19
# Desc : implement the game of hangman using previously developed
#        helper functions
# File : hangman.py
###############################################################################

import string # for getting all lowercase letter in alphabet

###############################################################################
def main():
###############################################################################
    
    print ("Welcome to my game of Hangman")
    secretWord = 'mihir'
    lettersGuessed = ''
    while (isWordGuessed(secretWord, lettersGuessed) == False):
        print("You have the following letters available: " + getAvailableLetters(lettersGuessed))
        char = input("Guess a letter -->")
        if not char.isalpha():
            print("invalid input, please try again...")
            continue
        lettersGuessed += char
        if char not in secretWord:
            print("This letter is not in the word!")
        print("Available letters: " +  getAvailableLetters(lettersGuessed))
        print("Guessed Word:  " +  getGuessedWord(secretWord, lettersGuessed))

    print ("You guessed it, good job!")
            
        
# main()

###############################################################################
def isWordGuessed(secretWord, lettersGuessed):
############################################################################### 
   is_guess_right = False
   for char in secretWord:
       if char in lettersGuessed:
           is_guess_right = True
       else:
           is_guess_right = False
           break
   return is_guess_right
       
# isWordGuessed()

###############################################################################
def getGuessedWord(secretWord, lettersGuessed):
############################################################################### 
   guessed_word = ''
   for char in secretWord:
       if char not in lettersGuessed:
           guessed_word += '_'
       else:
           guessed_word += char
           
   return guessed_word
       
# getGuessedWord()

###############################################################################
def getAvailableLetters(lettersGuessed):
############################################################################### 
    alphas = list(string.ascii_lowercase)
    for char in alphas: 
        if char in lettersGuessed:
            alphas.remove(char)

    retstr = ''.join(alphas)
    return retstr
              
# getAvailableLetters()

if __name__ == "__main__":
    main()
