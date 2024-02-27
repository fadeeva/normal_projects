import random
import pickle
from typing import List, Set, Dict, Tuple


with open('deck.pickle', 'rb') as f:
    deck = pickle.load(f)

DECK_LEN = 52

deck_in_game = deck.copy()
random.shuffle(deck_in_game)

number_of_players = int(input('Enter number of players 1-5: '))
if number_of_players > 5 or number_of_players < 1:
    number_of_players = 1

players = [[] for i in range(number_of_players)]

def calculate_points(cards:List)->int:
    points = 0
    for card in cards:
        if card[1:] in ['J', 'Q', 'K']:
            points += 10
        elif card[1:] == 'A':
            points += 1
        else:
            points += int(card[1:])
    
    return points


while True:
    for i in range(number_of_players):
        if len(deck_in_game):
            card = deck_in_game[random.randint(0, len(deck_in_game)-1)]
            players[i].append(card)
            print_players = ' '.join(players[i])
            print(f'Player #{i+1}: {print_players}  | {calculate_points(players[i])} |')
            deck_in_game.remove(card)
        else:
            print('We have run out of cards')
            break

    move = input('More(m), Stop(s), Player #n stop(ns) ').split(',')
    if move[0] == 's':
        break


            


    