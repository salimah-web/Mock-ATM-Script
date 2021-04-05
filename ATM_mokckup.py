from datetime import datetime
from random import randint
database= {4636547679:['salima','sally',2000],4523418944:['bilal','billy',6000]}


def generate_account_number():
    x=''
    for i in range(10):
        y=randint(0,9)
        x=x+str(y)
    return x


def bank_operations(user_details):
    print('')
    print('These are the available options:')
    print('1.Withdrawal\n2.cash deposit\n3.Complaint\n4.account balance')
    
    selected_option=input('Please select an option\n>>>')
    print('')
    if int(selected_option) == 1:
        amount=eval(input('How much would you like to withdraw?\n>>>'))
        if database[user_details][2]>= amount:
            print('take your cash')
            print(f'Current balance is {database[user_details][2]-amount}')
        else:
            print('insufficient funds')
    elif int(selected_option) == 2:
        amount=eval(input('How much will you like to deposit?\n>>>'))
        print('Your account has been credited')
        print(f'Current balance is {database[user_details][2]+amount}')
        
    elif int(selected_option) == 3:
        complaint = input('What issue will ypu like to report?\n>>>')
        print('Thank you for contacting us.')

    elif int(selected_option) == 4:
        print(f'Your account balance is {database[user_details][2]}')

    else:
        print('Invalid option, please try again')
        bank_operations(user_details)
    

def login():
    print('')
    print(datetime.now())
    print('Fill in your login details')
    
    account_no=int(input('type in your account number\n>>>'))
    password = input('type in your password\n>>>')
    
    if account_no in database and database[account_no][1]==password:
        print(f'Welcome {database[account_no][0]}')
        bank_operations(account_no)
    else:
        print('invalid account number or password')
        login()

def register():
    print('')
    print(datetime.now())
    print('REGISTRATION')
    details=[]
    name= input('Full name:\n>>>')
    password = input('Password?\n>>>')
    account_balance=0.0
    
    details.append(name)
    details.append(password)
    details.append(account_balance)
    print(details)
    Account_number=generate_account_number()
    print(Account_number)
    print(f'You have succesfully registered to our bank, Your account number is {Account_number} ')
    database[int(Account_number)]=details
    print(database)
    

def homepage():
    print('')
    print(datetime.now())
    print('Welcome to GTBank')
    option = int(input('Enter 1 to create an account\nEnter 2 to sign in\n>>>'))

    if option == 1:
        register()
    elif option == 2:
        login()
    else:
        print('invalid input')
        homepage()


homepage()
option = 1
while option == 1:
    option = int(input('would you like to carry out another operation?\n1. yes\n2.no\n>>>'))
    if option == 1:
        login()

    elif option == 2:
        print('Thank you for banking with us!!')
