import os
import pandas as pd

from .entry import Entry
from .character import Character
from .player import Player

class Study:
    """
    A representation of the main study.

    The study created a list of characters and their attributes.
    """

    sources = os.path.join(os.path.dirname(os.path.realpath(__file__)), "sources")
    partial_survey = os.path.join(sources, "sept15_partial_survey.xlsx")
    mappings = {
        "Timestamp": "Timestamp",
        "What is your age?": "Player Age",
        "With what gender do you identify? (Use \"other\" to self-describe)": "Player Gender",
        "What is the highest degree or level of education you've completed?": "Player Education",
        "How long have you been playing D&D?": "Player Experience",
        "What's your character's name?": "Name",
        "When did you last play this character?": "Recentness",
        "What gender does your character identify as? (Use other to self-identify)": "Gender",
        "What is your character's age in years?": "Age",
        "Did this character die?": "Is Dead",
        "What race is your character?": "Race",
        "What classes are your character?": "Classes",
        "What subclass is your character?": "Subclass",
        "What level is your character?": "Level",
        "Can you predict when your character will level up?": "Not Milestone",
        "What's your character's alignment?": "Alignment",
        "How did you generate your initial ability scores for this character?": "Gen Method",
        "Were you able to choose to which ability you assigned each score?": "Scores Assigned",
        "What is your character's strength (STR) ability score?": "STR",
        "What is your character's dexterity (DEX) ability score?": "DEX",
        "What is your character's constitution (CON) ability score?": "CON",
        "What is your character's intelligence (INT) ability score?": "INT",
        "What is your character's wisdom (WIS) ability score?": "WIS",
        "What is your character's charisma (CHA) ability score?": "CHA",
        "What is your character's Hit Points?": "HP",
        "What is your character's Armor Class?": "AC",
        "To the nearest 1gp, how much gold does your character have?": "Gold",
        "With which skills does your character have proficiency?": "Skills",
        "I enjoy the roleplaying aspects of D&D": "Player RP Enjoyment",
        "I enjoy the mechanical aspects of D&D": "Player Mechanical Enjoyment",
        "The character I built above was designed to be as mechanically optimal as possible": "Player Character Optimization",
        "(Optional) Tell me about your character!": "Description",
        "Add any additional comments here / tell me about the survey experience :)": "Meta",
    }

    character_attrs = ['Name', 'Recentness', 'Gender', 'Age', 'Is Dead',
       'Race', 'Classes', 'Subclass', 'Level', 'Not Milestone', 'Alignment',
       'Gen Method', 'Scores Assigned', 'STR', 'DEX', 'CON', 'INT', 'WIS',
       'CHA', 'HP', 'AC', 'Gold', 'Skills', 'Description']

    def __init__(self, entries, df=None):
        """
        Creates a study from the entries
        """
        self.entries = entries
        if df is None:
            self._get_df_from_entries()
        else:
            self.df = df

    @classmethod
    def from_file(cls, fname):
        """
        Creates a study given the filename
        """
        df = pd.read_excel(fname)
        df = df.rename(mapper=cls.mappings, axis=1)
        entries = []
        for i, _ in enumerate(df.iloc):
            row = df.iloc[i].to_dict()
            character = Character(**{k: v for k, v in row.items() if k in cls.character_attrs})
            player = Player(**{k: v for k, v in row.items() if k not in cls.character_attrs})
            entry = Entry(character, player)
            entries.append(entry)
        return cls(entries, df)


study = Study.from_file(Study.partial_survey)
