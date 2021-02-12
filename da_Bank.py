# This is a simple banking program that allows the user to
# deposit, withdraw , and check balance
#
class Bank_account:
    def __init__(self):
        self.balance = 2000

    def deposit_amount(self):
        deposit = int(input('Enter the amount to deposit: '))
        self.balance = self.balance + deposit

        print(''' The deposit was successful.
        Your new balance is $ %f''' % self.balance)

    def withdraw_amount(self):
        withdrawal = int(input('Enter the amount to withdraw: '))
        if withdrawal < self.balance:
            self.balance = self.balance - withdrawal
            print(''' The withdrawal was successful.
                 Your new balance is $ %f''' % self.balance)
        else:
            print('You cannot withdraw more than what you have')

    def check_balance(self):
        print('Your current balance is $ %f' % self.balance)


acc = Bank_account()
response = 'y'
account_number = input('Please enter your account number ')

while response == 'Y' or response == 'y':
    selection = input('Hello account number: ' + str(account_number) + ''' Welcome to the  Omni bank. 
    Please enter a number to perform a certain transaction'
    1. Deposit
    2. Withdrawal
    3. Check Balance
    4. Exit 
    ''')
    if int(selection) == 1:
        acc.deposit_amount()

    elif int(selection) == 2:
        acc.withdraw_amount()

    elif int(selection) == 3:
        acc.check_balance()

    elif int(selection) == 4:
        print(str(account_number) + 'Thanks for banking with us')
        break

    else:
        print('Invalid entry!')

    response = input('''Would you like to perform another transaction?
    please type in Y or y for yes. Type any other character for no.
    ''')
    if response != 'Y' and response != 'y':
        print(str(account_number) + 'Thanks for banking with us')
        break


