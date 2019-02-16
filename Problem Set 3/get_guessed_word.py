#!/usr/bin/env python

###############################################################################
# Name : Mihir Patel
# Date : 2/15/19
# Desc :implement the function getGuessedWord that takes in two parameters
#       - a string, secretWord, and a list of letters, lettersGuessed.
#       This function returns a string that is comprised of letters and
#       underscores, based on what letters in lettersGuessed are in
#       secretWord
# File : get_guessed_word.py
###############################################################################

###############################################################################
def main():
###############################################################################
    secretWord = 'apple'
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(getGuessedWord(secretWord, lettersGuessed))
# main()

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

if __name__ == "__main__":
    main()
