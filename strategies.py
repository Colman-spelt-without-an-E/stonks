import numpy as np
from framework import TradingBotPaper

class MA_MR_naive(TradingBotPaper):
    """
    Child class representing a naive mean reversion strategy using moving average,
    ie. buy 1 unit when current price < moving average, sell 1 unit when current price > moving average

    Parameters
    ----------
    order : int
            order of simple moving average model
    weight_type : str
                  weight type of moving average model;
                  "simple" for simple moving average model, "exp" for exponential moving average model
    a : float
        degree of weighting decrease of exponential moving average model;
        between 0 and 1
    *args
        passed to TradingBotPaper class
    **kwargs
        passed to TradingBotPaper class
    """

    def __init__(self, order=5, a=0.125, weight_type="simple", *args, **kwargs):
        """
        Create attributes.

        Attributes
        ----------
        ma : float
             current moving average, does not include current price
        ma_history : list
                     stores the historic moving averages starting from p_history for exponential moving average model;
                     stores the historic moving averages starting from present for simple moving average model
        """
        super().__init__(*args, **kwargs)
        self.weight_type = weight_type

        if self.weight_type == "simple":
            self.order = order
            self.ma_history = []

        if self.weight_type == "exp":
            self.a = a
            self.ma = self.p_history[0]
            self.ma_history = [self.ma]
            for p in self.p_history[1:-1]:
                self.ma = self.a * p + (1 - self.a) * self.ma
                self.ma_history.append(self.ma)

    def buy_sell(self):
        # compute moving average
        if self.weight_type == "simple":
            window = self.p_history[-self.order:]
            self.ma = np.mean(window)

        elif self.weight_type == "exp":
            self.ma = self.a * self.p_history[-1] + (1 - self.a) * self.ma

        self.ma_history.append(self.ma)

        if self.p < self.ma:
            return 1
        elif self.p == self.ma:
            return 0
        else:
            return -1