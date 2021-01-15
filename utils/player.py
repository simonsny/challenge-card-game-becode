from utils.card import Card
from random import randrange


class Player:

    def __init__(
            self,
            name: str,
            cards: list = None,
            turn_count: int = 0,
            number_of_cards: int = 0,
            history_cards: list = None,
            active_card: Card = None,
    ):
        """
        :param name: Name of the player in string
        :param cards: List containing the cards a player holds
        :param turn_count:
        :param number_of_cards:
        :param history_cards:
        :param active_card:
        """
        self.name = name
        if cards == None:
            cards = []
        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        if history_cards == None:
            history_cards = []
        self.history_cards = history_cards
        self.active_card = active_card

    def play(self):
        """
        Method that will return one randomly picked card from the cards that the Player still holds.
        """
        if not self.cards:
            print('No cards left.')
            return
        if self.active_card:
            self.history_cards.append(self.active_card)
        self.active_card = self.cards.pop(randrange(len(self.cards)))
        print(f"{self.name} {self.turn_count} played: {self.active_card}")
        self.number_of_cards -= 1
        self.turn_count += 1
        return self.active_card

    def add_card(self,card):
        """
        Function takes as input a card and appends it to the players' list of cards.

        :param card: The card to be added to the list.
        """
        self.cards.append(card)
        self.number_of_cards += 1

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'Player name: {self.name}, turn_count: {self.turn_count}, number_of_cards: {self.number_of_cards}, \
        history: {[str(card) for card in self.history_cards]},\n cards: {self.cards}'
