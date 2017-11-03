import unittest
import pandas

def create_test_dataframe_from_csv(filename):
    df = pandas.read_csv(filename)
    df['start_date'] = pandas.to_datetime(df['start_date'])
    df['end_date'] = pandas.to_datetime(df['start_date'])
    return df

class TestElectionInit(unittest.TestCase):
    def setUp(self):
        test_csv = 'test-polls-00.csv'
        self.df = create_test_dataframe_from_csv(test_csv)

    

if __name__ == '__main__':
    unittest.main()