## More on moving average (MA) model using mean reversion strategy

In this section, we try different **buy functions**. 

Recall the naive mean reversion MA model buys one share when current price is lower than the moving average, and sells one share when current price is higher than the moving average. Mathematically, this buy function is the sign function $sgn(x)=1$ for $x>0$, $sgn(x)=-1$ for $x<0$, and $sgn(x)=0$ for $x=0$. Below is the naive buy function plotted on a graph (left), and the corresponding trade history (right) by applying EMA onto Google's share price. 

<p align="center">
  <img src="graphs/buy_func_ind.png" width=40% height=40%>
  <img src="graphs/ma_mr_exp_sgn_goog_diff_no_ma.png" width=40% height=40%>
</p>

Instead of a sign function, what about a linear function? The figure below shows the graph of $y=x$ (left), and the corresponding trade history (right) using this buy function. 

<p align="center">
  <img src="graphs/buy_func_id.png" width=40% height=40%>
  <img src="graphs/ma_mr_exp_id_goog_diff_no_ma.png" width=40% height=40%>
</p>

Similarly, for a logarithmic function $f(x) = \ln(1+x)$ for $x \geq 0$, and $f(x) = -\ln(1-x)$ for $x<0$, 
<p align="center">
  <img src="graphs/buy_func_odd_log.png" width=40% height=40%>
  <img src="graphs/ma_mr_exp_oddlog_goog_diff_no_ma.png" width=40% height=40%>
</p>

arctan $f(x)=\arctan(x)$, 
<p align="center">
  <img src="graphs/buy_func_arctan.png" width=40% height=40%>
  <img src="graphs/ma_mr_exp_arctan_goog_diff_no_ma.png" width=40% height=40%>
</p>

square root $f(x)=\sqrt{x}$ for $x \geq 0$, and $f(x)=-\sqrt{x}$ for $x<0$, 
<p align="center">
  <img src="graphs/buy_func_oddsqrt.png" width=40% height=40%>
  <img src="graphs/ma_mr_exp_oddsqrt_goog_diff_no_ma.png" width=40% height=40%>
</p>

and just for fun, an exponential function $f(x) = e^x-1$ for $x \geq 0$, and $f(x) = 1-e^{-x}$ for $x<0$. 
<p align="center">
  <img src="graphs/buy_func_odd_exp.png" width=40% height=40%>
  <img src="graphs/ma_mr_exp_oddexp_goog_diff_no_ma.png" width=40% height=40%>
</p>

Since we can always scale the buy function by a constant factor, we are not particularly interested in the flat value of profit/loss, but rather the relative *dips* and *dunks* of it. What metric should we use to evaluate performance? Well, the best machine trades the *least* to gain the most profit. In other words, I would like to buy and sell as little shares as possible to maximise gain. Mathematically, the metric 
$$\text{profit per share traded (PPST)} =\frac{\text{net worth at the end}}{\text{total no. of shares bought and sold all throughout}}$$
is used. 

<p style="font-style: italic; font-size: 9pt">
  As far as I know, this metric is not used in any literature. I apologise beforehand in case 1) there is a better metric to use and I missed it, or arguably worse, 2) this metric <b>is</b> used, but with a different name.
</p>

It can actually be shown that PPST is invariant under positive scalar multiplication to the buy function, ie. PPST remains the same when we multiply the buy function by a positive constant. The proof is not important to our cause and will be skipped. *Just believe me.*

The figures below plot the PPST against the degree of weighting decrease for different companies with varying buy functions. As usual, for all simulations, closing prices of the past 16 days are given (to compute the exponential moving average), and the machine trades once per day for 101 days. Circled is the point with highest PPST. 

<p align="center">
  <img src="graphs/ma_mr_exp_goog_ppst.png" width=49% height=49%>
  <img src="graphs/ma_mr_exp_amzn_ppst.png" width=49% height=49%>
  <img src="graphs/ma_mr_exp_msft_ppst.png" width=49% height=49%>
  <img src="graphs/ma_mr_exp_aapl_ppst.png" width=49% height=49%>
</p>

Three features stand out immediately:
1. The identity buy function (id) performs well. In fact, id scores the highest PPST with the right degree of weighting decrease inside the interval $[0.05, 0.3]$.
2. 
    a. The sign buy function (sgn) and exponential function (exp-like) are the most inconsistent as degree of weighting varied. 

    b. Logarithmic (log-like), arctan (arctan), and square root (sqrt-like) functions behave somewhat consistently as degree of weighting varied. They are also quite similar to each other. This is expected as the functions themselves are quite similar to each other. 
3. Things are ***weird*** with Amazon. 

<img src=https://www.redherring.com/wp-content/uploads/2017/11/9489389920_b640002265_b-720x400.jpg width=30% height=30%>

It sounds absurd, but let's difference Amazon's corresponding time series again. Below shows the second difference time series (left) and the PSST against the degree of weighting decrease with varying buy functions (right). 

<p align="center">
  <img src="graphs/amzn_differenced2_time_series.png" width=43% height=43%>
  <img src="graphs/ma_mr_exp_amzn_diff2_ppst.png" width=55% height=55%>
</p>

Now it makes more sense. 

Takeaways for this section on MA model using mean reversion: 
1. The metric PPST is introduced to evaluate the performance of a trading strategy. 
2. Taking second difference of a time series might make it more stationary. 
3. Although the identity buy function works quite well, it never hurts to try different buy functions, and with varying degrees of weighting decrease too. 