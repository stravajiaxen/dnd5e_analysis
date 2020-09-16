class Player(dict):
    """
    A Player is a person who answered the survey and their thoughts :D
    """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
