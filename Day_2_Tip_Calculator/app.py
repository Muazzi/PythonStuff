# Tip Calculator
print("Welcome to the tip calculator.")
bill = float(input('What was the total bill?$'))

people = int(input('How many people to split the bill?'))

tip = float(input('What percentage tip would you like to give ?'))
tip = tip/100
tip = 1 + tip
amount = round(bill / people*tip,2)
print(f"Each person should pay : ${amount}")
