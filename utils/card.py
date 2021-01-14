class Symbol:
    """
    Class that will be the parent class of Card, holding the color and icon.
    """

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
        return f"{self.color} {self.icon}"

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
        return f"{self.color} {self.icon} {self.value}"

