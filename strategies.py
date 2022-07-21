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
        
class MA_MR(TradingBotPaper):
    """
    Child class representing a mean reversion strategy using moving average, 
    with additional control on units to buy depending on the difference between current price and moving average. 
    
    Parameters
    ----------
    order : int
            order of simple moving average model
    a : float
        degree of weighting decrease of exponential moving average model;
        between 0 and 1
    weight_type : str
                  weight type of moving average model; 
                  "simple" for simple moving average model, "exp" for exponential moving average model
    buy_func : str or function
               function of one argument;
               takes the difference between current price and moving average and returns the unit of shares to buy/sell,
               positive buys, negative sells; 
               default "ind", representing the indicator function of 
               buying 1 share when current price < moving average, and selling 1 vice versa
    *args
        passed to TradingBotPaper class
    **kwargs
        passed to TradingBotPaper class
    """
    def __init__(self, order=5, a=0.125, weight_type="simple", buy_func="ind", *args, **kwargs):
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
        self.buy_func = buy_func
        
        if self.weight_type == "simple":
            self.order = order
            self.ma_history=[]
        
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
        
        if self.buy_func == "ind":        
            if self.p < self.ma:
                return 1
            elif self.p == self.ma:
                return 0
            else:
                return -1
        
        if callable(self.buy_func):
            d = self.ma - self.p
            return self.buy_func(d)
        else:
            raise TypeError("buy_func not callable")
