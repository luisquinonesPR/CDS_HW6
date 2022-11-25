import pandas as pd
from sklearn.ensemble import RandomForestClassifier


class Model:
    def __init__(self, feat_cols: pd.DataFrame, targ_col: pd.Series):
        self.feat_cols_ = feat_cols
        self.targ_col_ = targ_col

    def train(self, reg):
        self.reg = reg
        model_ = RandomForestClassifier()
        self.fit = model_.fit(self.feat_cols_, self.targ_col_)

    def predict(self, data: pd.DataFrame):
        self.data = data
        self.predict_proba = self.fit.predict_proba(self.data)
        return self.predict_proba
