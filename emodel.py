import pandas as pd
import numpy as np
import datetime

data_dir = 'huffpo-gov-2012-2016/'

class Election:
    """Input

    """

    def __init__(self, election_day: str, polls: pd.DataFrame, choices: list):
        self.election_day = datetime.datetime.strptime(election_day, '%Y-%m-%d')
        self.days_remaining = (election_day - datetime.datetime.today()).days

        self.polls = polls

        # Candidates, ballot measures, etc.
        # Includes "other"
        # Excludes "undecided" and "refused"
        self.choices = choices

        # Fill nan in undecided with: 100 - sum(choices)
        if 'undecided' in self.polls.columns:
            self.polls['undecided'].fillna(
                100 - polls[choices].fillna(0).sum(axis=1),
                inplace=True)









