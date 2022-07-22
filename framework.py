class TradingBotPaper:
    """
    A class representing a trading bot on paper with analysis tools.

    Parameters
    ----------
    capital : float
              capital starting off with
    share : float
            shares possessed starting off
    past : list
           (known) past time series up until present, non-inclusive;
           used to determine action buy/sell
    future : list
             future time series, present inclusive;
             used to determine action buy/sell
    future_price : list
                   future share prices, present inclusive;
                   used to compute capital, shareholder value, and net worth
    """

    def __init__(self, past, future, future_price=None, capital=0, share=0):
        """
        Construct attributes.

        Attributes
        ----------
        t : int
            present time index
        x : float
            present time series entry
        p : float
            current price

        past : list
               (known) past time series up until present, non-inclusive
        future : list
                 future time series, present inclusive;
                 used to determine action buy/sell
        future_price : list
                       future share prices, present inclusive;
                       used to compute capital, shareholder value, and net worth

        buy_history : list
                      stores historical buys each day;
                      positive buys, negative sells

        capital : float
                  capital
        capital_history : list
                          stores historical capital

        share : float
                share possessed
        share_history : float
                        stores historical shares possessed

        shareholder_val : float
                          shareholder value
        shareholder_val_history : list
                                  stores historical shareholder values

        net_worth : float
                    net worth;
                    ie. how much you have in total if you sell all assets at present
        net_worth_history : list
                            stores historical net worth
        """

        self.t = 0
        self.x = future[0]
        self.past = past
        self.future = future
        if future_price is None:
            self.future_price = self.future
        else:
            self.future_price = future_price
        self.p = self.future_price[0]

        self.buy_history = []

        self.capital = capital
        self.capital_history = [self.capital]

        self.share = share
        self.share_history = [self.share]

        self.shareholder_val = self.share * self.p
        self.shareholder_val_history = [self.shareholder_val]

        self.net_worth = self.shareholder_val + self.capital
        self.net_worth_history = [self.net_worth]

    def buy(self):
        # overwrite this
        pass

    def _update(self):
        "With current price p per unit of asset, update attributes after buying or selling, depending on buy_sell"
        outcome = self.buy()
        self.share += outcome
        self.capital -= outcome * self.p
        self.shareholder_val = self.share * self.p
        self.net_worth = self.capital + self.shareholder_val

        # update time, time series entry, and price
        self.t += 1
        self.x = self.future[self.t]
        self.p = self.future_price[self.t]

        # update histories
        self.buy_history.append(outcome)
        self.past.append(self.x)
        self.capital_history.append(self.capital)
        self.share_history.append(self.share)
        self.shareholder_val_history.append(self.shareholder_val)
        self.net_worth_history.append(self.net_worth)

    def simulate(self, T):
        """
        Perform trades at every time interval for T times.
        """
        while self.t < T:
            self._update()