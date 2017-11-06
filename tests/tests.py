import unittest

import datetime
import pandas

import sys
sys.path.append('..')

import emodel


def create_test_dataframe_from_csv(filename):
    df = pandas.read_csv(filename)
    df['start_date'] = pandas.to_datetime(df['start_date'])
    df['end_date'] = pandas.to_datetime(df['end_date'])
    return df


class TestElectionInit(unittest.TestCase):
    def setUp(self):
        test_csv = 'test-polls-00.csv'
        df = create_test_dataframe_from_csv(test_csv)
        self.responses= ['response0', 'response1', 'undecided', 'other']
        self.election = emodel.Election(df)

    def test_init(self):
        self.assertIsInstance(self.election, emodel.Election)
        self.assertIsInstance(self.election.polls, pandas.DataFrame)

    def test_set_responses(self):
        self.election.set_responses(self.responses)
        self.assertEqual(self.election.responses, ['response0', 'response1', 'other',])
        self.assertEqual(self.election.responses_uncertain, ['undecided'])

    def test_set_interest(self):
        interest = ['response0', 'response1']
        self.election.set_interest(interest)
        self.assertEqual(self.election.interest, ['response0', 'response1'])

    def test_set_election_day_str(self):
        self.election.set_election_date('2016-11-08')
        self.assertEqual(self.election.election_date, datetime.datetime.strptime('2016-11-08', '%Y-%m-%d'))

    def test_set_election_day_datetime(self):
        dt = datetime.datetime.strptime('2016-11-08', '%Y-%m-%d')
        self.election.set_election_date(dt)
        self.assertEqual(self.election.election_date, datetime.datetime.strptime('2016-11-08', '%Y-%m-%d'))

    def test_days_remaining_with_past_date(self):
        dt = datetime.datetime.strptime('2016-11-08', '%Y-%m-%d')
        self.election.set_election_date(dt)
        self.assertEqual(self.election.days_remaining, pandas.Timedelta('0 days').days)

    def test_days_remaining_with_future_date(self):
        dt = datetime.datetime.strptime('2100-11-08', '%Y-%m-%d')
        self.election.set_election_date(dt)
        days_remaining = (dt - datetime.datetime.now()).days
        self.assertEqual(self.election.days_remaining, days_remaining)

    def test_undecided_fill_missing(self):
        self.election.set_responses(self.responses)
        self.election._fillnan_undecided()
        self.assertEqual(self.election.polls['undecided'].sum(), 25.0)




class TestWeights(unittest.TestCase):
    def setUp(self):
        test_csv = 'test-polls-00.csv'
        df = create_test_dataframe_from_csv(test_csv)
        #self.responses= ['response0', 'response1', 'undecided', 'other']
        self.election = emodel.Election(df)
        self.election.set_election_date('2016-11-08')

        self.weights = emodel.Weights(self.election)

    def test_days_until_election(self):
        self.assertEqual(self.weights.weights['days_until_election'].tolist(), [1, 2, 2, 2, 5, 6, 7, 7, 8, 8])

    def test_exp_decay_rate(self):
        """Rate of a 30 day halflife exponential decay"""
        self.assertEqual(emodel.Weights.exp_decay_rate(30), -0.023104906018664842)

    def test_exp_decay_weight(self):
        decay_rate = emodel.Weights.exp_decay_rate(30)
        self.assertEqual(emodel.Weights.exp_decay_weight(days=30, decay_rate=decay_rate), 0.5)


if __name__ == '__main__':

    unittest.main()