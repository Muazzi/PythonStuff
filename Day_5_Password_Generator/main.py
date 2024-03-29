#Password Generator Project
import random
import string
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

all_characters = string.ascii_letters + string.digits + string.punctuation
pass_length = nr_letters+nr_symbols+nr_numbers

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
random_letters = random.choices(letters,k=nr_letters)
random_numbers = random.choices(numbers,k=nr_numbers)
random_symbols = random.choices(symbols,k=nr_symbols)
password = random_letters+random_symbols+random_numbers
passwordVal= ''.join(password)
print('Easy password')
print(passwordVal)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
print('random order')
password_hard = random.choices(all_characters,k=pass_length)
passwordHardVal= ''.join(password_hard)
print(passwordHardVal)
