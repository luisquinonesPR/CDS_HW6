import pandas as pd
from abc import ABCMeta, abstractmethod
from sklearn.preprocessing import StandardScaler, PolynomialFeatures

class Transform(metaclass = ABCMeta):
    def __init__(self, df: pd.DataFrame):
        self.df = df

    @abstractmethod
    def change(self):
        return NotImplementedError

class Standardize(Transform):
    def change(self):
        scaler = StandardScaler()
        scaled_df = scaler.fit_transform(self.df)
        self.scaled = pd.DataFrame(scaled_df, columns = self.df.columns, index = self.df.index)

class Polynomial(Transform):
    def change(self, poly):
        poly = PolynomialFeatures(poly)
        poly_df = poly.fit_transform(self.df)
        poly_cols = poly.get_feature_names_out(self.df.columns)
        self.poly = pd.DataFrame(poly_df, columns = poly_cols, index = self.df.index)
