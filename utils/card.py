class Symbol:
    """
    Class that will be the parent class of Card, holding the color and icon.
    """
    color_code = {'red': "\033[1;31;40m", 'black': "\033[1;37;40m", 'normal': '\033[0m'}

    def __init__(self, color: str, icon: str):
        """
        :param color: Holds the color of a Card
        :param icon: Holds the Icon of a Card
        """
        self.color = color
        self.icon = icon

    def __repr__(self):
        return repr({"color": self.color, "icon": self.icon})

    def __str__(self):
        return f"{Symbol.color_code[self.color]} {self.icon} {Symbol.color_code.normal}"

class Card(Symbol):
    """
    Class that inherits from Symbol, used to create cards and hold the symbol and value of a card
    """

    def __init__(self, color, icon, value):
        """
        :param color: The color of a card
        :param icon: The Icon of a card
        :param value: The Value of a card
        """
        super().__init__(color, icon)
        self.value = value

    def __repr__(self):
        return repr({"color": self.color, "icon": self.icon, "value": self.value})

    def __str__(self):
        return f"{Symbol.color_code[self.color]} {self.icon}{self.value} {Symbol.color_code['normal']}"

card1 = Card('red', 'red', 1)
card2 = Card('black', 'black', 2)
card3 = Card('normal', 'normal', 3)

print(card1, card3)
print(card2)