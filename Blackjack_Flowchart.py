'''
@author: Abraham Milgram
Description: Player vs dealer blackjack
Created on Oct 12, 2021
'''
import random

def main():
    
    card = []
    suits = ['♠', '♣', '♥', '♦']


    player = []
    dealer = []
    pdisplay = []
    ddisplay = []
    
    # Gives 2 cards to player & dealer
    o = [player, dealer]
    for j in o:
        j.append(card_gen())
        j.append(card_gen())
    
    # Assigns suits to the cards so they can be displayed
    for u in o:

        for p in u:
            a = []
            random.shuffle(suits)
            a.append(p)
            a.append(suits[0])

            if u == player:
                pdisplay.append(a)
            elif u == dealer:
                ddisplay.append(a)
    
    # Displays Cards
    print(f'You have a {pdisplay}')
    print(f'Dealer shows {ddisplay[0]}')

    player_play(player, dealer)

def player_play(player, dealer):

    while True:

        # If the player has 21 they win
        if sum(player) == 21: 
            winloss('pwin')
            quit()

        else:
            # Asks to hit or stand
            hitstand = input("Hit or Stand? ").lower()
            if hitstand == 'hit':
                # Assigns another card and detects loss
                card = card_gen()
                print(f"You got an {card}!")
                player.append(card)
                if sum(player) > 21:
                    winloss('ploss')
                    quit()
            # If they stand move to dealer play
            elif hitstand == 'stand':
                dealer_play(dealer, player)

def dealer_play(dealer, player):
    # Detects if dealer wins
    if sum(dealer) == 21:
        winloss('dwin')
        quit()
    
    else:
        while True:
            # If the dealer is greater than 16 draw a card + detects loss
            if sum(dealer) < 16:
                dealer.append(card_gen())
                if sum(dealer) > 21:
                    winloss('dloss')
                    quit()
                else:
                    dealer_play(dealer, player)
            # Whichever player has more wins
            else:
                if sum(player) >= sum(dealer):
                    winloss('pwin')
                    quit()
                else:
                    winloss('dwin')
                    quit()

# Prints win or loss statements 
def winloss(dpwl):
    if dpwl == 'pwin' or dpwl == 'dloss':
        print('Player Wins!')
    elif dpwl == 'dwin' or dpwl == 'ploss':
        print('Dealer Wins!')

# Card generation
def card_gen():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

    for a in range(2):
            random.shuffle(cards)
            return cards[0]

if __name__ == '__main__':
    main()