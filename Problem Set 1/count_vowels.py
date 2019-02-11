# -*- coding: utf-8 -*-
###############################################################################
# Name : Mihir Patel
# Date : 2/11/19
# Desc : Assume s is a string of lower case characters.
#        Write a program that counts up the number of vowels contained 
#        in the string s. 
#        Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
#        For example, if s = 'azcbobobegghakl', your program should print 5.
# File : count_vowels.py
###############################################################################

###############################################################################
def main():
###############################################################################
    print(count_vowels('azcbobobegghakl'))
# main()

###############################################################################
def count_vowels(s):
###############################################################################
    s = s.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    num_of_vowels = 0
    for i in  range(0, len(s)):
        if s[i] in vowels:
            num_of_vowels += 1
    return num_of_vowels
# count_vowels()
            
if __name__ == "__main__":
    main()

