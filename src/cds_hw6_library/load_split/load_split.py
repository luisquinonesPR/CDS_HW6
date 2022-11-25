import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

class Load_Split:
    def __init__(self, data: str):
        self.df = pd.read_csv(data)
        self.train, self.test = sklearn.model_selection.train_test_split(self.df, test_size=0.5)
