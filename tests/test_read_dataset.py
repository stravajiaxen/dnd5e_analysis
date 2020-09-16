import unittest
from cbs_survey.study import latest_study
import matplotlib.pyplot as plt


class ReadDataset(unittest.TestCase):

    def test_read(self):
        plt.hist(latest_study.df["CHA"])
        plt.show()

if __name__ == '__main__':
    unittest.main()
