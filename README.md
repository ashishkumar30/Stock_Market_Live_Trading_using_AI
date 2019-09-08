# Zerodha_Live_Automate_Trading-_using_AI_ML_on_Indian_stock_market

* Online trading using Artificial Intelligence Machine leaning with python on Indian Stock Market, trading using live bots indicators screener and backtesters using rest api and websocket.

* Zerodha    - Automated Python program for trading in Indian stock market.      Worked individually on an Automated live project of Indian stock market for live trade, an automated python program which trade automatically on Indian stock market NSE/BSE using screener, indicators and backtester with our own strategy. Screener is a python program which sort the top stocks of Indian market and then we trade on that sorted stocks, and indicator is a program which shows the phase of Indian market or trend of market, And after that when we get the sorted stock then we backtest the particular stock before trading on it through our backtesting program which backtest it on historical data of few months and then find the probability of the profit and loss on that stock or we can say that we predict the future of market.Using screener ,indicator, backtester and our own strategy we made our Automated live bot which trade automatically in Indian stock market through Zerodha, an online broker using API of Zerodha kite and library KiteConnect we access the historical data of Indian Stock Market and after analyzing the historical data of stock Market, we made our bot using screener indicator backtest with our own strategy and place orders on Indian stock exchange to get profits through different strategy and Indicators made by us using numpy pandas and matplotlib .while working on this project I made so many indicators on Indian stock market like SMA, EMA ,Bollinger Band, RSI ,ATR and GUPPY etc.  And Stock market Screener “RSI Screener ” and “Guppy Screener”. Some of my live working buy/sell bots are “RSI BOT” and “GUPPY BOT” which trade automatically started automatically for trading on NIFTY_50 , future stocks etc in morning at 9:15 and end trading on 3:15 and shows the result PnL, profit/loss and all the orders and full result of day in csv file etc. 

* Kite Connect is a set of REST-like HTTP APIs that expose many capabilities required to build a complete stock market investment and trading platform. It lets you execute orders in real time (equities, commodities, mutual funds), manage user portfolios, stream live market data over WebSockets, and more.Zerodha is an Indian financial service company (member of NSE, BSE, MCX, MCX-SX),that offers retail and institutional broking, currencies and commodities trading, mutual funds, and bonds. Founded in 2010, Zerodha is known for its discount pricing model and technology. It is headquartered in Bengaluru and has physical presence in all major Indian cities.
As of 2019.

* Files ()

* 1. Getting Started with Zerodha ,Starting new project with zerodha :- Login to zerodha, Finding " Instrument Token list of zerodha, Finding a token from symbol,INPUTS, Getting HISTORICAL DATA,Getting continous data of stock,for last trade price of stock, for last ohlc of stock, FOR PLACING AN ORDER, Cancel an order, Exit from an order, Order Placed information, Open positions, Holdings you have, Websocket, Websocket threading, STATUS of order from websocket.

2. BACKTESTIG_PROGRAM == What is Backtesting?
Zerodha backtesting is a trading strategy that is based on historical data, where traders use past data to see how a strategy would have performed. The definition of a backtesting application is a set of technical rules applied to a set of historical price data, and the subsequent analysis of the returns that a Zerodha strategy would have generated over a specific period of time.
Backtesting is a type of program that allows traders to test potential trading strategies using historical data. The program recreates the behaviour of trades and their reaction to a Zerodha trading strategy, and the resulting data can then be used to measure and optimise the effectiveness of a given strategy before applying it to real market conditions. Backtesting strategies work on the assumption that trades that have performed successfully in the past will perform well in the future

3. Historical Data Download Code for any stock of Stock Market;- This code will download historical data of any stocks or multiple stocks in csv

4.Stock_Screener (GUPPY)== What is Stock_Screener ?
A stock screener is a tool to shortlist few companies from a pool of all the listed companies on a stock exchange using filters on the basis of indicator result (RSI,GUPPY,SMA,).shows the result of buy and sell stocks, which one is better option for buy or sell .The investors specify the filters and the stock screener gives the results accordingly. Stock screeners are very useful as it can save you a lot of time.You do not need to go through all the listed companies to shortlist few good ones. You can just apply the basic filter to get the list of few good ones that you want to investigate further. Overall, the stock screener will help you to find good performing stocks according to your specifications with a single click.

5.INDICATORS (ATR,RSI,SMA,EMA,Bollinger band ) on Historical_data 'SBI'
* What Is a Technical Indicator?
Technical indicators are heuristic or mathematical calculations based on the price, volume, or open interest of a security or contract used by traders who follow technical analysis. By analyzing historical data, technical analysts use indicators to predict future price movements. Examples of common technical indicators include the Relative Strength Index, Money Flow Index, Stochastics, MACD and Bollinger Bands®.

* How Technical Indicators Work ?
Technical analysis is a trading discipline employed to evaluate investments and identify trading opportunities by analyzing statistical trends gathered from trading activity, such as price movement and volume. Unlike fundamental analysts, who attempt to evaluate a security's intrinsic value based on financial or economic data, technical analysts focus on patterns of price movements, trading signals and various other analytical charting tools to evaluate a security's strength or weakness. Technical analysis can be used on any security with historical trading data. This includes stocks, futures, commodities, fixed-income, currencies, and other securities. In this tutorial, we’ll usually analyze stocks in our examples, but keep in mind that these concepts can be applied to any type of security. In fact, technical analysis is far more prevalent in commodities and forex markets where traders focus on short-term price movements. Technical indicators, also known as "technicals", are focused on historical trading data, such as price, volume, and open interest, rather than the fundamentals of a business, like earnings, revenue, or profit margins. Technical indicators are commonly used by active traders, since they're designed to analyze short-term price movements, but long-term investors may also use technical indicators to identify entry and exit points.

6. Live_Trading_BOTS==What is a Trading BOT ?
* A Zerodha trading robot is a computer program based on a set of indian trading signals that helps determine whether to buy or sell a currency pair at a given point in time. Zerodha robots are designed to remove the psychological element of trading, which can be detrimental. While trading systems can be purchased online, traders should exercise caution when buying them this way.
Trading bots are widely available programs that connect to a user’s indian exchange and make trades on their behalf. They work using a variety of indicators and signals, such as moving averages and indices. The idea is simple: to help users make money in the markets, while not wasting a lot of their time. The underlying assumption is that computers are much better at trading than humans could ever be, because trading is all about mathematics and complex calculations of probability.

7.Trading Live BOT (1) == BUY-SELL BOT on RSI strategy
About this Trading BOT
This is the automated BUY and SELL code for zerodha , it will buy order and sell that order on indian exchange based on buy/sell strategy implemented on code.Place an order when RSI is greater then 30,when high breaks next high,place BUY SL order on current high when BUY SL order implemented on ZERODHA place an order of SELL on lowest lowcand if RSI cross70:cancel the SELL SL bid place MARET order of BUY bid.Full strategy mention below.

8.Trading Live BOT (2)==GUPPY strategy bot
About this Trading BOT
This is a small program which first scan all the stocks using guppy Screener and sort all the buy and sell stocks in timeframe of 5, 10,15 minutes and shows the result. after it will find the common stock from all timeframe of buy and sell and then we have to enter a stock from above list to run the buy/sell program. and it will buy a stock on green signal from indicator and on red signal sell a stock 

9. Trading Live BOT (3) == automated bot of BUY-SELL bot on Guppy indicator 4 colours
About this Trading BOT
This is the automated BUY and SELL code for zerodha , it will first scan all the tokens on guppy indicator using screener on 5 minute 15 minute and 30 minute and shows the result of buy sell from all 3 timeframe and after the token which is high priority of buy /sell will sort out and then we have to select on which stock we want to rrun our bot at which timefrme quantity and exchange. we can place order any stock which we want .

10.Trading Live BOT (4) == Advance Multiple bot of buy/sell in one BOT with screener, backtestig
About this Trading BOT
Screener is implemented. 
backtesting is implemented in it on last 6 (or any) working days of zerodha 
shows all the orders and profit and loss at 3 pm
multiple trade at same time
BOT STRATEGY:-This is an advance bot , this code start buy trade on when indicator gives green signal and sell on red signal , and sell a stock on red signal of indicator and buy when it gives green signal. this bot trade on multiple stocks at same time , all other bots work only on one stock at a time, but this bot will work on multiple stocks at a time. it will first scan all the stocks of nifty 50 and when it gets any of buy/sell stock it wil place order and manage that stock it can trade on multiple stock at same time and continue monitoring all stocks

11. Trading Live BOT (5)== FULL automated bot on GUPPY indicator
About this Trading BOT
start bot with 2 inputs of buy/sell and timeframe then it will scan all the stock and automatically pick the best stock among all the stock and place order on the best stock and continue with it . if u want to run bot you can continue bot without scanning and run normal bot also.
