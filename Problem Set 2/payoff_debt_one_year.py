#!/usr/bin/env python

##################################################################
# Name : Mihir Patel
# Date : 2/12/19
# Desc : a program that calculates the minimum fixed monthly
#        payment needed in order pay off a credit card balance
#        within 12 months. By a fixed monthly payment, we mean
#        a single number which does not change each month, but
#        instead is a constant amount that will be paid
#        each month.
# File : payoff_debt_one_year.py
##################################################################

##################################################################
def main():
##################################################################
    original_balance = 3926
    annual_interest_rate= 0.2
    monthly_interest_rate = annual_interest_rate / 12
    monthly_payment = 0
    keepCalculating = True
    
    while (keepCalculating):
        
        # keep incrementing by 10 to find the lowest fixed monthly payment
        # since it has to be multiple of 10
        
        monthly_payment += 10
        # we're trying again, so reset the balance value to orignal.
        balance =  original_balance
        
        # let's see if this monthly payment is sufficent
        for i in range(0, 12):
            monthly_unpaid_balance = balance  - monthly_payment
            balance = monthly_unpaid_balance + (monthly_interest_rate  * monthly_unpaid_balance)
            
            if balance <= 0:
                keepCalculating = False
                break
            
    print("Lowest payment: " + str(monthly_payment))

# main()

if __name__ == "__main__":
    main()
