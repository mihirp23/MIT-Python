#!/usr/bin/env python

##################################################################
# Name : Mihir Patel
# Date : 2/12/19
# Desc : a program that uses these bounds and bisection search
#        (for more info check out the Wikipedia page on
#        bisection search) to find the smallest monthly payment
#        to the cent (no more multiples of $10) such that we can
#        pay off the debt within a year. Try it out with large
#        inputs, and notice how fast it is (try the same
#        large inputs in your solution to Problem 2 to compare!).
#        Produce the same return value as you did in Problem 2.
# File : payoff_debt_using_bisection.py
##################################################################

##################################################################
def main():
##################################################################
    original_balance = 999999
    annual_interest_rate= 0.18
    monthly_interest_rate = annual_interest_rate / 12
    monthly_payment = 0
    
    
    lower_bound = original_balance / 12
    upper_bound = (original_balance * ((1 + monthly_interest_rate) ** 12)) / 12.0
    
    
    
    while (lower_bound <= upper_bound):
        
        # midpoint
        monthly_payment = (lower_bound + upper_bound) / 2
        
        # set the balance variable to original value
        balance =  original_balance
        
        # let's see if this monthly payment is sufficent
        for i in range(0, 12):
            monthly_unpaid_balance = balance  - monthly_payment
            balance = monthly_unpaid_balance + (monthly_interest_rate  * monthly_unpaid_balance)
        
        print ("upper bound : " + str(upper_bound))
        print ("lower bound : " + str(lower_bound))
        print (balance)
        
        
        # adjust our upper and lower bounds according to the calculated balance
        if balance < 0:
            upper_bound = monthly_payment
            lower_bound = lower_bound + 1
        else:
            lower_bound = monthly_payment
            upper_bound = upper_bound - 1
        
    print("Lowest payment: " + str(format(monthly_payment, '.2f')))    

# main()

if __name__ == "__main__":
    main()
