import pandas as pd
import numpy as np
import datetime
import math

data_dir = 'huffpo-gov-2012-2016/'

class Election:
    """Input

    """

    def __init__(self, polls: pd.DataFrame):
        self.election_day = None
        self.days_remaining = None

        self.polls = polls

        # Includes any response of uncertainty: "undecided"
        # TODO: include "refused" and exclude from self.responses
        self.responses_uncertain = None
        # Candidates, ballot measures, etc.
        # Includes "other", etc.
        self.responses = None

        self.interest = None


    def _fillnan_undecided(self):
        # Fill nan in undecided with: 100 - sum(choices)
        if 'undecided' in self.polls.columns:
            self.polls['undecided'].fillna(
                100 - self.polls[self.responses].fillna(0).sum(axis=1),
                inplace=True)

            # Remove negatives
            self.polls['undecided'].clip_lower(0)

    def set_election_day(self, election_day):
        if type(election_day) is datetime.datetime:
            self.election_day = election_day
        elif type(election_day) is str:
            self.election_day = datetime.datetime.strptime(election_day, '%Y-%m-%d')

        self.days_remaining = (self.election_day - datetime.datetime.today()).days

        if self.days_remaining < 0:
            self.days_remaining = 0

    def set_interest(self, interest):
        """
        :param interest: List of column names that represent poll responses of interest.
        :return:
        """
        self.interest = interest.copy()

    def set_responses(self, responses):
        """
        :param responses: List of any column names that represent poll responses.
        :return:
        """
        self.responses = list()
        for resp in responses:
            if resp == 'undecided':
                self.responses_uncertain = ['undecided']
            else:
                self.responses.append(resp)


    def inspect_data(self):
        print('Columns with null values:')
        print(self.election.polls.isnull.any())


class Weighted:

    def __init__(self, election: pd.DataFrame):
        pass

    @staticmethod
    def exp_decay_rate(halflife: int):
        """Calculate a rate to be used for an exponential decay function"""
        return math.log(1/2) / halflife

    @staticmethod
    def exp_decay_weight(days, decay_rate):
        """Calculate a weight based on days passed using a specific rate of decay,
        the decay weight is exponential with more recent having a higher weight
        """
        return math.e**(decay_rate * days)

















