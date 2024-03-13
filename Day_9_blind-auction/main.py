import locale
import  art
import  os
clear = lambda : os.system('cls')
loc = locale.setlocale(locale.LC_ALL, '')
conv = locale.localeconv()
print(art.logo)
print("Welcome to the secret auction program. ")
bidders = {}
name = input('What is your name?:')
bid = float(input(f"What's your bid?:{conv['currency_symbol']}  "))
bidders[name] =bid
ans = ''.casefold()
ans = input("Are there any other bidders? Type 'yes' or 'no'.")
print("\033[H\033[3J", end="")

while ans != 'no':
    name = input('What is your name?')
    bid = float(input(f"What's your bid?:{conv['currency_symbol']}  "))
    bidders[name] = bid
clear()
highest_bidderName = max(bidders.keys(),key = bidders.get)



print(f"The winner is {highest_bidderName} with a bid of {conv['currency_symbol']} {bidders[highest_bidderName]}")

