# -*- coding: utf-8 -*-
###############################################################################
# Name : Mihir Patel
# Date : 2/11/19
# Desc : Assume s is a string of lower case characters.
#        Write a program that prints the longest substring of s in which 
#        the letters occur in alphabetical order. For example, 
#        if s = 'azcbobobegghakl', then your program should print 'beggh'
#        In the case of ties, print the first substring
# File : longest_substr.py
###############################################################################

###############################################################################
def main():
###############################################################################
    s = 'abcbcd'
    print (get_longest_sorted_substr(s))    
# main()

###############################################################################
def get_longest_sorted_substr(s):
###############################################################################
    s = s.lower()
    substr = list(s[0])
    longest_substr = ''
    for i in range(1, len(s)):
        if substr[-1] <= s[i]:
            # the character is greater than previous
            # ie. still sorted alphabetically
            substr.append(s[i])
        else:
            # not sorted alphabetically until now.
            # so, begin a new one
            substr = list(s[i])
        
        # keep comparing the current string to the max 
        # If greater, then replace
        if len(longest_substr) < len(substr):
                longest_substr = substr

    return longest_substr
# get_longest_sorted_substr()

if __name__ == "__main__":
    main()
    