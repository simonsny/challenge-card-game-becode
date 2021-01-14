from utils.player import Player
from utils.deck import Deck


class Board:
    def __init__(self, players):
        self.players = players
        self.turn_count = 0
        self.history_cards = []
        self.deck = Deck()
        self.active_cards = []

    def start_game(self):
        self.input_players()
        self.deck.fill_and_distribute(self.players)

        i = 0
        while len(self.history_cards) < 52:
            print(f'\n********** BEGINNING OF ROUND {self.turn_count} **********\n')

            print('Turn count:', self.turn_count)
            i+= 1
            for player in self.players:
                player.play()
                self.active_cards.append(player.active_card)
                print(player)
                print('\n')
            print(f'Active cards: {self.active_cards}')
            #print('\n\n')
            self.turn_count += 1
            self.history_cards.extend(self.active_cards)
            self.active_cards = []
            print(f'\n************* END OF ROUND {self.turn_count-1} *************\n')
            #print('\n\n')
        '''
        while game is going
            make each player play a card
            print(turn count)
            print active cards
            print number of cards in history cards'''

    def input_players(self):
        """
        Asks for the users to input the players' names and puts them in a the players list.
        """
        print("Please input all players here one by one.\nWe need at least 2 players and max 52. \
        \nPress 'Enter' in a blank feeld to start the game.")
        i = 1
        while i <= 52:
            input_string = input(f'Player {i}: ')
            print()
            if input_string == "":
                if len(self.players) < 2:
                    print("Please enter a name.")
                    continue
                break
            self.players.append(Player(input_string))
            i += 1


if __name__ == '__main__':
    board = Board([])
    board.start_game()
    for player in board.players:
        print(player)
