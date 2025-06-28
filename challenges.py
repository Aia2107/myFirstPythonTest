#final challenge: create a program that simulates an ATM withdrawal.
#Allow the user to enter an amount to withdraw.
#If the amount is not a valid number, raise a ValueError.
#If the amount is greater than the available balance, raise an InsufficientFundsError.  
#always display the remaining balance at the end of the program.

account_balance = 1500

try:
    withdraw_amount = int(input('How much would you like to withdraw?'))
    if withdraw_amount > account_balance:
        print('Insufficient funds for this withdrawal.')
    else:
        account_balance -= withdraw_amount
except ValueError:
    print('Invalid input. Please enter a valid number.')
finally:
    print(f'Your remaining balance is: {account_balance}')