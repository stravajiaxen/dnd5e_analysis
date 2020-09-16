class Entry:
    """
    A single entry in the survey. It's a character and a player
    """

    def __init__(self, character, player):
        """
        Sets the character and the player
        """

        self.character = character
        self.player = player
