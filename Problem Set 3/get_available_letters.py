#!/usr/bin/env python

###############################################################################
# Name : Mihir Patel
# Date : 2/16/19
# Desc : implement the function getAvailableLetters that takes in one parameter
#        - a list of letters, lettersGuessed. This function returns a string
#       that is comprised of lowercase English letters - all lowercase
#       English letters that are not in lettersGuessed
# File : get_available_letters.py
###############################################################################

import string # for getting all lowercase letter in alphabet

###############################################################################
def main():
###############################################################################
    
    lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
    print(getAvailableLetters(lettersGuessed))
# main()

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
