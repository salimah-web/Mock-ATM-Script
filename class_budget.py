# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 14:48:37 2021

@author: salima omari
"""


class Budget:
    def __init__(self,category,balance ):
        self.category= category
        self.balance = balance
    def withdraw(self):
        amount= float(input('how much will you like to withdraw?'))
        if amount<=self.balance:
            self.balance-=amount
            print('Take your cash!!!')
        else:
            print('insufficient funds!!')
        
    def deposit(self):
        amount= float(input('how much will you like to deposit?'))
        self.balance+=amount  
        print(f'Deposit successful, {self.balance}')
        
    def available_balance(self):
        print(f'You have {self.balance}')
        
    def transfer(self,target):
        amount=float(input('how much will you like to transfer?'))
        if amount<=self.balance:
            self.balance-=amount
        
            target.balance+=amount
            print("transfer successful")
        else:
            print('insufficient funds')

food=Budget('food',3000)
clothing=Budget('clothing', 800)
entertainment=Budget('entertainment', 500)

food.transfer(entertainment)
entertainment.available_balance()
food.available_balance()
