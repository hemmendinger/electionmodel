import unittest
import pandas

import sys
sys.path.append('..')

import emodel


def create_test_dataframe_from_csv(filename):
    df = pandas.read_csv(filename)
    df['start_date'] = pandas.to_datetime(df['start_date'])
    df['end_date'] = pandas.to_datetime(df['start_date'])
    return df

class TestElectionInit(unittest.TestCase):
    def setUp(self):
        test_csv = 'test-polls-00.csv'
        df = create_test_dataframe_from_csv(test_csv)
        self.election = emodel.Election(df)

    def test_init(self):

        self.assertIsInstance(self.election, emodel.Election)
        self.assertIsInstance(self.election.polls, pandas.DataFrame)

    def test_set_responses(self):
        responses= ['response0', 'response1', 'undecided', 'other']
        self.election.set_responses(responses)
        self.assertEqual(self.election.responses, ['response0', 'response1', 'other',])
        self.assertEqual(self.election.responses_uncertain, ['undecided'])

    def test_set_interest(self):
        interest = ['response0', 'response1']
        self.election.set_interest(interest)
        self.assertEqual(self.election.interest, ['response0', 'response1'])



if __name__ == '__main__':

    unittest.main()