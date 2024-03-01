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
stop_list_players = []


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


def is_possible_add_to_stop_list(command: str)->bool:
    if len(command) == 2 and command[-1] == 's':
        try:
            players_id = int(command[0])
            return True
        except:
            return False


def add_player_to_stop_list(command:str)->bool:
    if is_possible_add_to_stop_list(command):
        stop_list_players.append(int(command[0])-1)
        return True
    return False
    

def execute_command(command:List)->bool:
    if len(command) > 0:
        for i in command:
            if i == 's':
                return False
            elif i == 'm':
                return True
            elif not add_player_to_stop_list(i):
                yes_or_no = input('Bad command. Continue game?(y/n) ') # check it
                if yes_or_no == 'n':
                    return False
                elif yes_or_no == 'y':
                    continue
            else:
                continue
    return True


while True:
    for i in range(number_of_players):
        if len(deck_in_game) and i not in stop_list_players:
            card = deck_in_game[random.randint(0, len(deck_in_game)-1)]
            players[i].append(card)
            deck_in_game.remove(card)
        else:
            if not len(deck_in_game):
                print('We have run out of cards')
            elif number_of_players == len(stop_list_players):
                print('Dealer cards: ')
                break
        
        print_players = ' '.join(players[i])
        print(f'Player #{i+1}: {print_players}  | {calculate_points(players[i])} |')

    command = input('More(m), Stop(s), Player #n stop(ns) ').split(' ')
    if execute_command(command):
        continue
    break
    
            
