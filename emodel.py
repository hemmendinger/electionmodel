import pandas as pd
import numpy as np
import datetime

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

            self.polls['undecided'].fillna(100 - self.polls[self.response].fillna(0).sum(axis=1), inplace=True)
            #self.polls['undecided]

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

















