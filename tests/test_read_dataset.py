import unittest
from cbs_survey.study import study
import matplotlib.pyplot as plt


class TestReadDataset(unittest.TestCase):

    def test_read(self):
        plt.hist(study.df["CHA"])
        plt.show()

if __name__ == '__main__':
    unittest.main()
