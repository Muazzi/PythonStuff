import locale
import  art
import sys,subprocess
import decimal
from decimal import Decimal

clear = lambda : os.system('cls')
loc = locale.setlocale(locale.LC_ALL, '')
conv = locale.localeconv()
print(art.logo)
print("Welcome to the secret auction program. ")
bidders = {}
in_auction= False
#name = input('What is your name?:')
#bid = float(input(f"What's your bid?:{conv['currency_symbol']}  "))
#bidders[name] =bid
ans = ''.casefold()

#os.system('cls')

while not in_auction:
    name = input('What is your name?')
    bid = Decimal(input(f"What's your bid?:{conv['currency_symbol']}  "))
    bidders[name] = bid
    ans = input("Are there any other bidders? Type 'yes' or 'no'.")
    if ans == 'no':
        subprocess.run('cls', shell=True)
        in_auction = True

    if ans =='yes':
       subprocess.run('cls',shell = True)



highest_bidderName = max(bidders.keys(),key = bidders.get)
highest_bidder_value = round(bidders[highest_bidderName],2)



print(f"The winner is {highest_bidderName} with a bid of {conv['currency_symbol']} {highest_bidder_value}")

