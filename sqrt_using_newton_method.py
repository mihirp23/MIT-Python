#!/usr/bin/env python

## Mihir Patel
## Date : 2/17/19
## Calculate the square root of a number using
## Newton-Raphson method


############################################################
def sqrt_newton_raphson(num):
############################################################
    epsilon = 0.01 # tolerance level
    guess = num / 12 # starting guess

    while abs(guess * guess - num) >= epsilon:
        guess = guess - (((guess ** 2) - num) / (2 * guess))

    return guess

# sqrt_newton_raphson()

############################################################
def main():
############################################################
    while (True):
        num = input("Enter a number and I will calculate square root: ")
        if not num.isdigit():
            print("You did not enter a valid number, please try again!")
            continue
        else:
            print("Square root: " + str(sqrt_newton_raphson(int(num))))

# main()    
    
if __name__ == "__main__":
    main()
