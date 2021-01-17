from utils.player import Player
from utils.deck import Deck


class Board:
    def __init__(self):
        self.players = []
        self.turn_count = 0
        self.history_cards = []
        self.active_cards = []
        self.deck = Deck()

    def start_game(self):
        """
        Method of Board that starts the game.
        The game asks for the input of all players if not already entered previously.
        Next it fills the deck, shuffles and randomly distributes the cards to the players.
        Then the game will make each player play one card per turn, until no more cards are left.
        It is possible for some players to have one turn more then others.
        """

        self.input_players()
        self.deck.fill_and_distribute(self.players)
        i = 0
        for player in self.players:
            print(player)
        while len(self.history_cards) < 52:
            print(f'\n********** BEGINNING OF ROUND {self.turn_count} **********\n')
            print('Turn count:', self.turn_count)
            i += 1
            for player in self.players:
                player.play()
                self.active_cards.append(player.active_card)
                print(player)
                print('\n')
            print(f'Active cards: {" ".join([f"{p.name}: {c}" for p, c in zip(self.players, self.active_cards)])}')

            self.turn_count += 1
            self.history_cards.extend(self.active_cards)
            self.active_cards = []
            print(f'\n************* END OF ROUND {self.turn_count-1} *************\n')

    def create_deck(self) -> None:
        """
        Function that creates a deck inside the board
        """
        self.deck = Deck()

    def input_players(self):
        """
        Asks for the users to input the players' names and puts them in a the players list.
        """

        print("Please input all players here one by one.\nWe need at least 2 players and max 52. \
        \nPress 'Enter' in a blank feeld to start the game.")
        i = 1
        players = []
        while i <= 52:
            input_string = input(f'Player {i}: ')
            print()
            if input_string == "":
                if len(players) < 2:
                    print("Please enter a name.")
                    continue
                break
            players.append(input_string)
            i += 1
        self.players = [Player(name) for name in players]
