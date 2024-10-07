#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  5 21:26:55 2024

@author: jeffmarstell
"""
import random


def spin_row():
    symbols = [ '🍒', '🍉', '🍋', '🔔', '🌟']
    
    return [random.choice(symbols)for symbol in range(3)]

def print_row(row):
    print("•".join(row))

def get_payout(row, bet):
    if row[0] == row [1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '🌟':
            return bet * 20
    return 0
        
            
    

def main():
    balance = 100
    
    print("**************************")
    print("Wlcome to Python slaots!")
    print("Symobols: 🍒 🍉 🍋 🔔 🌟")
    print("**************************")
    
    while balance > 0:
        print(f"Current balance: ${balance}")
        
        bet = input("Place your be amount: ")
        
        if not bet.isdigit():
            print("Please enter a valid number")
            continue
        
        bet = int(bet)
        
        if bet > balance:
            print("insufficient funds.")
            continue
        
        if bet <= 0:
            print("bet must be greater than 0")
            continue
        
        balance -= bet
        
        row = spin_row()
        print("spinning...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("Sorry lost this round")

        balance += payout
        
        play_again = input("Do you want to spin again? (y/n): ").upper()

        if play_again != 'Y':
            break
    
    
    print("Game over your final balance is: {balance}")
    
    
if __name__ == '__main__':
    main()