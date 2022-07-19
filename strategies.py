import numpy as np
from framework import TradingBotPaper

class MA_MR_naive(TradingBotPaper):
    def __init__(self, base_wealth, p_history, p_future, order=5, asset=0):
        super().__init__(base_wealth, p_history, p_future, asset)
        self.order = order
    def buy_sell(self): 
        
        if len(self.p_history) < self.order:
            raise Exception("Not enough past price values to compute moving average. Try lowering order.")
            
        ave = np.mean(self.p_history[-self.order:])
        
        print(f"Moving average: {ave}")
        print(f"Closing price: {self.p}")
        
        if self.p < ave:
            return 1
        if self.p == ave:
            return 0
        else:
            return -1