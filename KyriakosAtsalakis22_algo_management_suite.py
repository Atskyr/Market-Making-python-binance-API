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

# convert timestamp to date format and ensure ohlcv are all numeric
df['date'] = pd.to_datetime(df['date'], unit='ms')
for col in df.columns[1:]:
    df[col] = pd.to_numeric(df[col])
    
df.tail()

closeminus2 = df.iloc[-3,4]
closeminus1 = df.iloc[-2,4]

openminus2 = df.iloc[-3,1]
openminus1 = df.iloc[-2,1]
low1 = df.iloc[-1,3]
high1 = df.iloc[-1,2]
df.tail()

        
        #sellentry1 = sellentry.astype(float)
        #sellentry2 = high1-sellentry1
        #sellentry3 = sellentry1-sellentry2


binance_client.futures_position_information(
    symbol='BTCUSDT')



op = pd.DataFrame(binance_client.futures_position_information(
    symbol='BTCUSDT',
    

    
))
sellentry = op.iloc[:2,2]
sellentry1 = sellentry.astype(float)
sellentry2 = sellentry1.iloc[-1]
sellentry3 = high1-sellentry2
sellentry4 = sellentry2-sellentry3
sellentry4=round(sellentry4, 3)

buyentry3 = sellentry2-low1
buyentry4 = sellentry2+buyentry3
buyentry4=round(buyentry4, 3)


op.iloc[:, :6]
op.columns = ['open', 'high', 'low', 'close', 'open', 'high', 'low', 'close', 'volume', 'po1so', 'op1en', 'hi1gh', 'lo31w', 'c1l3ose', 'v1olu3me']
op = op.iloc[:1,1]

#op = op.iloc[-1]
op = op.astype(float)
zero = 0
zeropoint = 0.0
op2 = op.iloc[-1]




if op2>zero:
        binance_client.futures_create_order(
     symbol='BTCUSDT',
     type='STOP_MARKET',
     side='SELL',
     stopPrice=low1,
     closePosition=True
     ) 

        
        

        binance_client.futures_create_order(
   symbol='BTCUSDT',
   type='STOP_MARKET',
   side='BUY',
   stopPrice=high1,
   closePosition=True
   ) 
    
elif op2<zero:
        binance_client.futures_create_order(
   symbol='BTCUSDT',
   type='STOP_MARKET',
   side='BUY',
   stopPrice=high1,
   closePosition=True
   ) 

        
        

        binance_client.futures_create_order(
     symbol='BTCUSDT',
     type='STOP_MARKET',
     side='SELL',
     stopPrice=sellentry4,
     closePosition=True
     )
        
  

op       
        