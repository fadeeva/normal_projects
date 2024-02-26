import random
from typing import List, Set, Dict, Tuple


deck = ['\u26602', '\u26603', '\u26604', '\u26605', '\u26606', '\u26607', '\u26608', '\u26609', '\u266010', '\u2660J', '\u2660Q', '\u2660K', '\u2660A', '\u26652', '\u26653', '\u26654', '\u26655', '\u26656', '\u26657', '\u26658', '\u26659', '\u266510', '\u2665J', '\u2665Q', '\u2665K', '\u2665A', '\u26662', '\u26663', '\u26664', '\u26665', '\u26666', '\u26667', '\u26668', '\u26669', '\u266610', '\u2666J', '\u2666Q', '\u2666K', '\u2666A', '\u26632', '\u26633', '\u26634', '\u26635', '\u26636', '\u26637', '\u26638', '\u26639', '\u266310', '\u2663J', '\u2663Q', '\u2663K', '\u2663A']

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


            


    