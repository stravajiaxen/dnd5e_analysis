class Character(dict):
    """
    A Character is a D&D character (who answered the survey :D)
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
