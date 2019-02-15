#!/usr/bin/env python

###############################################################################
# Name : Mihir Patel
# Date : 2/15/19
# Desc :implement the function isWordGuessed that takes in two parameters
#       - a string, secretWord, and a list of letters, lettersGuessed.
#       This function returns a boolean - True if secretWord has been
#       guessed (ie, all the letters of secretWord are in lettersGuessed)
#       and False otherwise.
# File : is_word_guessed.py
###############################################################################

###############################################################################
def main():
###############################################################################
    secretWord = 'apple'
    lettersGuessed = ['e', 'a', 'l', 'p', 'r', 's']
    print(isWordGuessed(secretWord, lettersGuessed))
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
       
# count_substr()

if __name__ == "__main__":
    main()
