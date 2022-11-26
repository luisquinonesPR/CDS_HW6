import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder




class Model:
    def __init__(self, feat_cols: pd.DataFrame, targ_col: pd.Series):
        self.__feat_cols_ = feat_cols
        self.__targ_col_ = targ_col
        lab = LabelEncoder()
        self.__targ_col_ = lab.fit_transform(self.__targ_col_)

    def train(self, reg):
        self.reg = reg
        model_ = RandomForestClassifier()
        self.fit = model_.fit(self.__feat_cols_, self.__targ_col_)

    def predict(self, data: pd.DataFrame):
        self.data = data
        self.predict_proba = self.fit.predict_proba(self.data)[:, 1]
        return self.predict_proba
