#!/usr/bin/env python

##################################################################
# Name : Mihir Patel
# Date : 2/12/19
# Desc : Program to calculate the credit card balance
#        after one year if a person only pays the minimum
#        monthly payment required by the credit card
#        company each month.
# File : payoff_debt.py
##################################################################

##################################################################
def main():
##################################################################
    balance = 42
    annual_interest_rate = 0.2
    monthly_payment_rate = 0.04
    monthly_interest_rate = annual_interest_rate / 12
    
    for i in range (0, 12):
        minimum_monthly_payment = monthly_payment_rate * balance
        monthly_unpaid_balance = balance - minimum_monthly_payment
        updated_balance = monthly_unpaid_balance + (monthly_interest_rate * monthly_unpaid_balance)
        balance = updated_balance
        print("Month " + str(i + 1) + " Remaining Balance: " + str(format(updated_balance, '.2f')))

# main()

if __name__ == "__main__":
    main()
