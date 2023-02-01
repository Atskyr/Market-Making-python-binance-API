import pandas as pd
#import asyncio
import pandas as pd
import pandas_ta as ta
from binance import BinanceSocketManager
from binance.client import Client
import os



user_key = 'gtDmBeJPjwWB1Fa8HbXTONxTrp7Ua0fbMs8lyiybzGjY2y35tUOsA6gVYnm3wUWk'
secret_key = 'u8BQkP0CJ0kCSXRjw1IYwqxQGiXRr2a0XFVg2AhRydsBHzY2MJtHK1OH7MD6IQcD'

binance_client = Client(user_key, secret_key)

# MARKET DATA
# current futures price
#binance_client.futures_coin_symbol_ticker(symbol='BTCUSD_PERP')

binance_client.futures_change_leverage(symbol='BTCUSDT', leverage=20)

#user_key = gtDmBeJPjwWB1Fa8HbXTONxTrp7Ua0fbMs8lyiybzGjY2y35tUOsA6gVYnm3wUWk
#secret_key = u8BQkP0CJ0kCSXRjw1IYwqxQGiXRr2a0XFVg2AhRydsBHzY2MJtHK1OH7MD6IQcD

#api_key = os.environ.get('gtDmBeJPjwWB1Fa8HbXTONxTrp7Ua0fbMs8lyiybzGjY2y35tUOsA6gVYnm3wUWk')
#api_secret = os.environ.get('u8BQkP0CJ0kCSXRjw1IYwqxQGiXRr2a0XFVg2AhRydsBHzY2MJtHK1OH7MD6IQcD')

#binance_client = Client(api_key, api_secret)

#binance_client.futures_symbol_ticker(symbol='BTCUSDT')

binance_client.futures_historical_klines(
    symbol='BTCUSDT',
    interval='30m',  # can play with this e.g. '1h', '4h', '1w', etc.
    start_str='2022-01-05',
    #end_str='2021-06-30'
)

df = pd.DataFrame(binance_client.futures_historical_klines(
    symbol='BTCUSDT',
    interval='30m',
    start_str='2022-01-05',
    #end_str='2021-06-30'
))
df.head()

# crop unnecessary columns
df = df.iloc[:, :6]
# ascribe names to columns

df.columns = ['date', 'open', 'high', 'low', 'close', 'volume']

df['close'] = df['close'].astype(float)


df["closeema"] = ta.ema(df["close"], length=50)

# convert timestamp to date format and ensure ohlcv are all numeric
df['date'] = pd.to_datetime(df['date'], unit='ms')
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col])
    
df.tail()

closeminus2 = df.iloc[-3,4]
closeminus1 = df.iloc[-2,4]

openminus2 = df.iloc[-3,1]
openminus1 = df.iloc[-2,1]

ema1 = df.iloc[-2,6]
ema2=round(ema1, 3)

    

#ff = df_test['open'].iloc[0]
#print()

#open1 = df.iloc[-1,4]
#print(open1)


#if ((closeminus2 > openminus2) and ((closeminus1 < openmimus1))
    
#binance_client.futures_create_order(
 #  symbol='BTCUSDT',
    #type='LIMIT',
    #timeInForce='GTC',  # Can be changed - see link to API doc below
    #price=46800,  # The price at which you wish to buy/sell, float
    #side='BUY',  # Direction ('BUY' / 'SELL'), string
    #quantity=0.0001  # Number of coins you wish to buy / sell, float
    
    
# limit order buy
if closeminus2 > openminus2 and closeminus1 < openminus1 and openminus1>ema2:
    print("xtupa! BUY! BUY! BUY!")
    binance_client.futures_create_order(
      symbol='BTCUSDT',
      type='STOP_MARKET',
      timeInForce='GTC',  # Can be changed - see link to API doc below
      stopPrice=closeminus2,  # The price at which you wish to buy/sell, float
      side='BUY',  # Direction ('BUY' / 'SELL'), string
      quantity=0.001  # Number of coins you wish to buy / sell, float
      )
    
else:
    
    print("den uparxei buy, " +
          "buydenyparxeikurie")
    

    # limit order sell
if closeminus2 < openminus2 and closeminus1 > openminus1 and openminus1<ema2:
    print("Xtupa! Sell! Sell! Sell!")
    binance_client.futures_create_order(
      symbol='BTCUSDT',
      type='STOP_MARKET',
      timeInForce='GTC',  # Can be changed - see link to API doc below
      stopPrice=closeminus2,  # The price at which you wish to buy/sell, float
      side='SELL',  # Direction ('BUY' / 'SELL'), string
      quantity=0.001  # Number of coins you wish to buy / sell, float
      )
      
else:
    
    print("den uparxei SELL, " +
          "SELLdenyparxeikurie")
    
    
print("zhse maimou")  
