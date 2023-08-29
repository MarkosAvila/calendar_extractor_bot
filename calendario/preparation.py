import pandas as pd


class ConvertNumber:
    """Convertir datos extraidos a valores númericos

    La lista deberá contener la información en este orden:
    [hours, importances, flags]
    """

    def __init__(self, dataframe) -> None:
        self.df = dataframe

    def clear_df(self):
        eliminar = self.df.loc[self.df[0] == "Todo el día"]
        self.df = self.df.drop(eliminar.index)
        self.df.reset_index(inplace=True, drop=True)
        self.df[0] = pd.to_datetime(self.df[0])

    def df_time_to_number(self):
        for i in range(self.df.shape[0]):
            hour = int(self.df.iloc[i, 0].hour)
            minute = int(self.df.iloc[i, 0].minute)
            minute = minute / 60
            self.df.iloc[i, 0] = hour + minute

    def df_currency_to_number(self):
        for i in range(self.df.shape[0]):
            match self.df.iloc[i, 2].strip():
                case "AUD":
                    self.df.iloc[i, 2] = 1
                case "CAD":
                    self.df.iloc[i, 2] = 2
                case "CHF":
                    self.df.iloc[i, 2] = 3
                case "EUR":
                    self.df.iloc[i, 2] = 4
                case "GBP":
                    self.df.iloc[i, 2] = 5
                case "JPY":
                    self.df.iloc[i, 2] = 6
                case "USD":
                    self.df.iloc[i, 2] = 7
                case "NZD":
                    self.df.iloc[i, 2] = 8

    def df_importance_to_number(self):
        for i in range(self.df.shape[0]):
            match self.df.iloc[i, 1].strip():
                case "Media":
                    self.df.iloc[i, 1] = 3
                case "Alta":
                    self.df.iloc[i, 1] = 4

    def df_day_to_number(self):
        self.df[3] = 0
        day = 0
        for i in range(self.df.shape[0]):
            if i > 0:
                if self.df.iloc[i, 0] >= self.df.iloc[i - 1, 0]:
                    self.df.iloc[i, 3] = day
                else:
                    day += 1
                    self.df.iloc[i, 3] = day
            elif i == 0:
                self.df.iloc[i, 3] = day
        self.df.drop(self.df[self.df[3] >= 5].index, inplace=True)