# -*- coding: utf-8 -*-

###############################################################################
# Name : Mihir Patel
# Date : 2/11/19
# Desc : Write a program that prints the number of times the 
#        string 'bob' occurs in s.
#        For example, if s = 'azcbobobegghakl', then your program 
#        should print 1.
# File : count_substr.py
###############################################################################

###############################################################################
def main():
###############################################################################
    print(count_substr('azcbobobegghakl', 'bob'))
# main()

###############################################################################
def count_substr(s, substr_to_check) :
############################################################################### 
   print(s)
   s = s.lower()
   count = 0
   substr = ''
   
   for i in range (0, len(s), 3):
       print(i)
       if i + 3 > len(s):
           exit
       else:
           print(substr)
           substr = s[i:i + 3]
           if substr == substr_to_check:
               count += 1
   return count
       
# count_substr()

if __name__ == "__main__":
    main()
