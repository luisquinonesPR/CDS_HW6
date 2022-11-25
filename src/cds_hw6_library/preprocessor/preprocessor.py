import pandas as pd

class PreProcessor:
 def __init__(self, df: pd.DataFrame):
    self.df = df

 def clean_rows(self, subset: list):
    self.cleaned = self.df.dropna(axis = 0, subset = subset)

 def fill_na_mean(self, cols: list):
    self.filled = self.df[cols].fillna(self.df.mean())
 
