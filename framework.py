import numpy as np

class TradingBotPaper:
    """
    A class representing a trading bot on paper with analysis tools. 
    
    Parameters
    ----------
    base_wealth : float
                  amount of wealth starting off with
    p_history : list or numpy array
                (known) prices at each time interval up until present, non-inclusive
    p_future : numpy array
               prices at each time interval starting from present inclusive
    asset : float
            units of asset currently in possession
    """
    def __init__(self, base_wealth, p_history, p_future, asset=0):
        """
        Construct attributes. 
        
        Attributes
        ----------
        p : float
            current price
        
        trade_history : list
                        stores historic trading outcomes of each day
        
        asset_wealth : float
                       asset wealth
        asset_history : list
                        stores historic asset
        asset_wealth_history : list
                               stores historic asset wealth after each trade
                        
        liquid_wealth : float
                        liquid wealth
        liquid_wealth_history : list
                                stores historic liquid wealth after each trade
                                
        total_wealth : float
                       total wealth, including liquidity and asset; 
                       ie. how much you have in total if you sell all assets at present
        total_wealth_history : list
                               stores historic total wealth after each trade        
                               
        outcome : float
              units to buy/sell;
                  positive means to buy, negative means to sell
        t : int
            present time index, usually in days
        """
        
        self.t = 0
        self.p_future = p_future
        self.p = self.p_future[self.t]
        self.p_history = p_history
        
        self.trade_history = []
        
        self.liquid_wealth = self.total_wealth = base_wealth
        self.liquid_wealth_history = [self.liquid_wealth]
        
        self.asset = asset
        self.asset_history = [self.asset]
        
        self.asset_wealth = asset * self.p
        self.asset_wealth_history = [self.asset_wealth]
        
        self.total_wealth = self.liquid_wealth + self.asset_wealth
        self.total_wealth_history = [self.total_wealth]
        
    def buy_sell(self):
        # overwrite this
        pass
    
    def trade(self):
        "With current price p per unit of asset, update attributes after buying or selling, depending on buy_sell"
        outcome = self.buy_sell()
        self.asset += outcome
        self.liquid_wealth -= outcome * self.p
        self.asset_wealth = self.asset * self.p
        self.total_wealth = self.liquid_wealth + self.asset_wealth
        
        # update time and price
        self.t += 1
        self.p = self.p_future[self.t]
        
        # update histories
        self.trade_history.append(outcome)
        self.p_history.append(self.p)
        self.liquid_wealth_history.append(self.liquid_wealth)
        self.asset_history.append(self.asset)
        self.asset_wealth_history.append(self.asset_wealth)
        self.total_wealth_history.append(self.total_wealth)
        
    def simulate(self, T):
        """
        Perform trades at every time interval for T times.
        """
        while self.t < T:
            self.trade()