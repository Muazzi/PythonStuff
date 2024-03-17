import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#How you will store the user's input.
def get_choice(val):
    choice = ''
    match val:
        case 0:
            choice = rock
        case 1:
            choice = paper
        case 2:
            choice = scissors

    return choice

def determine_winner(player,computer):
    if player == computer:
        print('Draw')
    if player == rock and computer == paper:
        print("Paper beats Rock Computer wins")
    elif player == paper and computer == rock:
        print("Paper beats Rock Player wins")
    elif player == scissors and computer == rock:
        print("Rock beats scissors Computer wins")
    elif player == rock and computer == scissors:
        print("Rock beats scissors Player wins")
    elif player == paper and computer == scissors:
        print("scissors beats paper computer wins")
    elif player == scissors and computer == paper:
        print("scissors beats paper Player wins")





player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if player_input >=3:
    print("Invalid choice game over!")
else:
    player_choice = ''
    computer_choice = ''
    # How you will generate a random choice for the computer.
    computer_input = random.randint(0, 2)
    player_choice = get_choice(player_input)
    computer_choice = get_choice(computer_input)
    print("Player choice:")
    print(player_choice)

    print("Computer choice:")
    print(computer_choice)
    determine_winner(player_choice, computer_choice)


