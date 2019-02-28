"""
Simple Moving Average implemented using KiteConnect Python library. -- [https://kite.trade](kite.trade)
Rainmatter (c) 2016
License
-------
This GIST is licensed under the MIT License
"""

from kiteconnect import KiteConnect 

# Initialize all the variables we need
api_key = "YOUR API KEY"
access_token = "YOUR ACCESS TOKEN"
client_id = "YOUR CLIENT ID"

# Instrument token of RELIANCE
instrument_token = "738561" 

# Dates between which we need historical data
from_date = "2016-10-01"
to_date = "2016-10-17"

# Interval(minute, day, 3 minute, 5 minute...)
interval = "5minute"

kite = KiteConnect(api_key=api_key)
kite.set_access_token(access_token)

# Gets historical data from Kite Connect
def get_historical_data():
	return kite.historical(instrument_token, from_date, to_date, interval)

"""
	 Implementation of the moving average strategy.
	 We go through the historical records that 
	 we received form Kite Connect, calculate moving average,
	 and place a BUY or SELL order.
"""
def strategy(records):
	total_closing_price = 0
	record_count = 0
	order_placed = False
	last_order_placed = None
	last_order_price = 0
	profit = 0

	for record in records:
		record_count += 1
		total_closing_price += record["close"]
		
		#Moving avearge is calculated for every 5 ticks(records)
		if record_count >= 5:
			moving_average = total_closing_price/5

			# If moving average is greater than last tick, place a buy order
			if record["close"] > moving_average:
				if last_order_placed == "SELL" or last_order_placed is None:
					
					# If last order was sell, exit the stock first
					if last_order_placed == "SELL":
						print "Exit SELL"

						# Calculate profit
						profit += last_order_price - record["close"]
						last_order_price = record["close"]

					# Fresh BUY order
					print "place new BUY order"
					last_order_placed = "BUY"

			# If moving average is lesser than last tick, and there is a position, place a sell order
			elif record["close"] < moving_average:
				if last_order_placed == "BUY":
					
					# As last order was a buy, first let's exit the position
					print "Exit BUY"
					
					# Calculate profit
					profit += record["close"] - last_order_price
					last_order_price = record["close"]
					
					# Fresh SELL order
					print "place new SELL order"
					last_order_placed = "SELL"
					

			
			total_closing_price -= records[record_count-5]["close"]
	print "Gross Profit ", profit
	# PLace the last order 
	place_order(last_order_placed)

# Place an order based upon transaction type(BUY/SELL)
def place_order(transaction_type):
	kite.order_place(tradingsymbol="RELIANCE", exchange="NSE", quantity=1, transaction_type=transaction_type, order_type="MARKET", product="CNC")


def start():
	records = get_historical_data()
	strategy(records)

start()