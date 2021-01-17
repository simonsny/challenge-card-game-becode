from utils.card import Card


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
        :param turn_count: Keeps track of the players turn
        :param number_of_cards: Number of cards
        :param history_cards: The History of cards the player has played
        :param active_card: The currently played card of the player
        """
        self.name = name.capitalize()
        if cards is None:
            cards = []
        self.cards = cards
        self.turn_count = turn_count
        self.number_of_cards = number_of_cards
        if history_cards is None:
            history_cards = []
        self.history_cards = history_cards
        self.active_card = active_card
        self.score = 0

    def play(self):
        """
        Method that will return one randomly picked card from the cards that the Player still holds.
        """

        if not self.cards:
            print('No cards left.')
            return
        if self.active_card:
            self.history_cards.append(self.active_card)
        i = self.choose_card_index()
        self.active_card = self.cards.pop(i)
        print(f"{self.name} {self.turn_count} played: {self.active_card}")
        self.number_of_cards -= 1
        self.turn_count += 1
        return self.active_card

    def add_card(self, card: Card):
        """
        Function takes as input a card and appends it to the players' list of cards.

        :param card: The card to be added to the list.
        """
        self.cards.append(card)
        self.number_of_cards += 1

    def choose_card_index(self) -> int:
        """
        Requests the user to input the index of the card in his hand he wants to play.
        :return: An integer that is the index of the card to play.
        """
        i = input(f"{self.name} choose a card you want to play: ")

        try:
            i = int(i)
            if i < 0 or i >= len(self.cards):
                print(f"Index must be between 0 and {len(self.cards)}")
                self.choose_card_index()
            return i
        except ValueError:
            print("ValueError: Input must a number")
            self.choose_card_index()

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'Player name: {self.name}, turn_count: {self.turn_count}, number_of_cards: {self.number_of_cards}' \
               f'\nHistory: {" ".join([str(card) for card in self.history_cards])}' \
               f'\nCards: {" ".join([str(card) for card in self.cards])}'
