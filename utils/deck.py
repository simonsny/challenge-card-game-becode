from random import shuffle as random_shuffle
from utils.card import Card

SYMBOLS = {'♥': 'red', '♦': 'red', '♣': 'black', '♠': 'black'}
VALUES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


class Deck:
    def __init__(self):
        self.cards = []

    def fill_and_distribute(self, players, shuffle_bool=True):
        """
        Combines the fill_deck en distribute methods in one for simple use.
        :param players: List of players to distribute cards to
        :param shuffle_bool: If True, shuffles the deck
        :return:
        """
        self.fill_deck()
        self.distribute(players, shuffle_bool)

    def fill_deck(self):
        """
        Method that takes no input and gives no ouput, fills the instance's deck with 52 cards.
        :return:
        """
        for symbol, color in SYMBOLS.items():
            for value in VALUES:
                self.cards.append(Card(color, symbol, value))

    def shuffle(self):
        random_shuffle(self.cards)

    def distribute(self, players: list, shuffle_bool: bool = True):
        """
        Distributes the cards between the players. By default it also shuffles the deck.

        :param players: List of all the players
        :param shuffle_bool: If True, shuffles the deck randomly.
        """
        if shuffle_bool:
            self.shuffle()
        for i in range(52):
            j = i % len(players)
            players[j].cards.append(self.cards[i])
            players[j].number_of_cards += 1

    def __repr__(self):
        return f"{deck.__dict__}"

    def __str__(self):
        return f"Deck filled with: {[str(card) for card in self.cards]}"
