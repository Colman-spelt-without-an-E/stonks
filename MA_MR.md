## More on moving average (MA) model using mean reversion strategy

The naive mean reversion MA model buys one share when current price is lower than the moving average, and sells one share when current price is higher than the moving average. Mathematically, this **buy function** returns 1 when moving average $-$ current price $>0$, returns -1 when moving average $-$ current price $<0$, and trivially returns 0 when moving average $-$ current price $=0$. 
<p align="center">
  <img src="graphs/buy_func_ind.png">
</p>
