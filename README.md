# Algorithmic trading

## Introduction

Algorithmic trading is the act of trading on the stock market using automated computer algorithms. It offers many advantages as opposed to manual trading: no (less) human error, consistent, continuous monitoring and trading, sensitive, etc. As more forms of trading like cryptocurrency surface, trading is becoming more and more accessible to the common person. There is a fast-growing market for people who want to invest but do not have the time to learn about the technicalities to it, and so the idea of selling trading bots is conceived. 

In this project, different trading strategies are investigated (well, lightly, since I'm a maths student after all and this project is fuelled by passion and interest, rather than the heavy expectation of an expert) and a trading bot is written in Python. (Again, since I'm very much a mathematician,) Detailed analysis is performed on said trading bot, and we compare it to other existing trading bots on the market. The final goal from then is to put our trading bot to test in the stock market. With real money. In real time. 


## Time series analysis

Fundamentally, the stock market functions is a time series. Although the stock market is notorious for its complexity and its near impossibility to predict, time series analysis still serves as a powerful tool for stock market forecasting. Much of the prior knowledge of what I am about to is covered extensively in "Analysis of Financial Time Series" by Tsay RS. Albeit old, this book is powerful introductory material to financial time series. 

For this part, the daily closing prices of Google, Amazon, Microsoft, and Apple ranging from 01/07/2019 to 31/12/2019 are investigated. This date range is chosen so the impact of COVID-19 can be dismissed. We plot the autocorrelation function against for each of the corporations. 
![goog_acf](https://user-images.githubusercontent.com/106886906/179564366-20b7d169-7479-41ef-8b65-7f0d4d3367f9.png)
![amzn_acf](https://user-images.githubusercontent.com/106886906/179564398-ca021617-538e-478a-8dcb-c54cbdf2636d.png)
![msft_acf](https://user-images.githubusercontent.com/106886906/179564401-91d7b011-1431-483e-9d14-cf9910baf780.png)
![aapl_acf](https://user-images.githubusercontent.com/106886906/179564411-b65c0cad-1fd9-4554-b892-941c198bbb63.png)
