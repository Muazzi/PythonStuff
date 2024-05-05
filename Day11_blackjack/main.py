import re
play_blackjack_input = input("Do you want to play a game of blackjack? Type 'y' or 'n':\n")
from logo import  logo
print(logo)
# how many cards in deck of cards ?
#ans :A "standard" deck of playing cards consists of 52 Cards in each of the 4 suits of Spades, Hearts, Diamonds, and Clubs.
# what collection will i use ?
#dictionary
#what will be the key of the dictionary ?
#suit_card ex s_2
# what wiil be the value ?
# numerical value
# dictionary of dictionaries
#generate values from 2-10

def deal(playercards,deck,dealer_cards):
    last_player_keys= list(playercards.keys())#[-1]
    last_player_key = last_player_keys[-1]
    key_prefix = "card"
    last_player_val = int(re.sub(key_prefix,"",last_player_key))
    last_player_val+=1
    key = key_prefix+str(last_player_val)
    dealer_card_value = deck[next(dealer_cards)]
    playercards[f'{key}'] =dealer_card_value
    return  playercards

#this function is going to take in the cards
# its going to look to check if there are aces in there
#if the index of the aces are not 0 and the sum of the values are not >=21 the new value will be 1
def check_for_aces(cards):
    # turning the cards keys into list
    cards_list = list(cards.keys())
    #here im summing the values
    cards_values = sum(cards.values())
    print(cards)
    print(f'card values : {cards_values}')
    #if the values >21
    if cards_values>21:
        res = {key: val for key, val in cards.items() if re.search("ace", key)}
        for k , v in res.items():
            cards[k]=1

    return  cards
#


#will need a empty dictionary called deck
deck_of_cards = {}
#function will take in the suit and create a set of cards with it its value

def generate_cards(suit):
    #adding the ace first
    deck_of_cards[suit+'_'+'ace'] = 11
    #adding the king
    deck_of_cards[suit + '_' + 'k'] = 10
    #added q
    deck_of_cards[suit + '_' + 'q'] = 10
    #added jack
    deck_of_cards[suit + '_' + 'j'] = 10
    for num in range(2,11):
        deck_of_cards[suit+'_'+str(num)] = num

    return deck_of_cards

generate_cards("spade") # generating spades
generate_cards("Hearts") # generating hearts
generate_cards("diamonds") # generating diamond
generate_cards("clubs") # generating clubs


# i should shuffle the cards
import  random as random
shuffled_cards = list(deck_of_cards.keys())
random.shuffle(shuffled_cards)
dealer_cards = iter(shuffled_cards)

# need a list for the player cards
player_cards ={}
computer_cards = {}
#take the first two cards from the deck
player_cards['card1'] = deck_of_cards[next(dealer_cards)]
player_cards['card2'] = deck_of_cards[next(dealer_cards)]
computer_cards['card1'] = deck_of_cards[next(dealer_cards)]

# i need to print Your cards : [value1 , val2ue]
player_card_values = list(player_cards.values())
computer_card_values = list(computer_cards.values())
in_game = False
while  not in_game:
    player_card_values = list(player_cards.values())
    computer_card_values = list(computer_cards.values())
    print(f"Your cards : {player_card_values}")
    print(f"Computers cards: {computer_card_values}")

    another_card_input = input("Type 'y' to get another card,type 'n' to pass \n")
    if another_card_input == 'y':
       player_cards= deal(player_cards,deck_of_cards,dealer_cards)
       player_cards = check_for_aces(player_cards)
       computer_cards= deal(computer_cards,deck_of_cards,dealer_cards)
       print(f"Your cards : {player_card_values}")
       print(f"Computers cards: {computer_card_values}")
       if sum(player_card_values) > 21:
           print('You lose')
    elif another_card_input == 'n':
        computer_cards = deal(computer_cards, deck_of_cards, dealer_cards)
        total_player_values = sum(player_card_values)
        total_computer_values = sum(computer_card_values)
        if total_player_values > total_computer_values & total_player_values < 21:
            print("You win!")
            in_game = True
        elif sum(player_card_values) < sum(computer_card_values):
            print("You lose")
            in_game = True
        else:
            print("Invalid input")












# busy with the deal function it needs to look at the digit at the end convert to an int and add 1 then generate a new key





