import random
import pickle
from typing import List, Set, Dict, Tuple


with open('deck.pickle', 'rb') as f:
    deck = pickle.load(f)

deck_in_game = deck.copy()
random.shuffle(deck_in_game)

number_of_players = int(input('Enter number of players 1-5: '))
if number_of_players > 5 or number_of_players < 1:
    number_of_players = 1

players = [[] for i in range(number_of_players)]
stop_list_players = []

dealer = []

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
                yes_or_no = input('Bad command. Continue game?(y/n) ')
                if yes_or_no == 'n':
                    return False
                elif yes_or_no == 'y':
                    continue
            else:
                continue
    return True


def get_card()->None:
    return deck_in_game[random.randint(0, len(deck_in_game)-1)]


def get_dealer_cards():
    for j in range(5):
        if len(deck_in_game):
            if calculate_points(dealer) > 17:
                break
            card = get_card()
            dealer.append(card)
            deck_in_game.remove(card)
            

def show_all_dealer_cards()->None:
    print_dealer = ' '.join(dealer)
    print('------------------------')
    print(f'Dealer cards:  {print_dealer}  | {calculate_points(dealer)} |')
    print('------------------------')


def show_player_cards(player_id:int)->None:
    print_players = ' '.join(players[player_id])
    print(f'Player #{player_id+1}: {print_players}  | {calculate_points(players[player_id])} |')


def show_winner()->None:
    players_points = []
    dealer_points = calculate_points(dealer)
    
    if dealer_points > 21:
        dealer_points = 0
    
    for i in players:
        p = calculate_points(i)
        if p > 21:
            p = 0
        players_points.append(p)
    
    print('------------------------')
    if dealer_points > max(players_points):
        print(f'WINNER: Dealer, with: {dealer_points}')
    else:
        print(f'WINNER: Player #{players_points.index(max(players_points)) + 1}')
    print('------------------------')
    


while True:
    for i in range(number_of_players):
        if i == 0 and len(dealer) == 0:
            card = get_card()
            dealer.append(card)
            deck_in_game.remove(card)
            
        if len(deck_in_game) and i not in stop_list_players:
            card = get_card()
            players[i].append(card)
            deck_in_game.remove(card)
        else:
            if not len(deck_in_game):
                print('We have run out of cards')
                break
            elif number_of_players == len(stop_list_players):
                break
        
        if calculate_points(players[i]) == 21: # govnokod
            stop_list_players.append(i)        # govnokod
        
        show_player_cards(i)
        
    show_all_dealer_cards()
    
    if number_of_players != len(stop_list_players):
        command = input('More(m), Stop(s), Player #n stop(ns) ').split(' ')
        if execute_command(command):
            continue
    
    get_dealer_cards()
    show_all_dealer_cards()
    show_winner()
    
    break
    
