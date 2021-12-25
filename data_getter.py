import pandas as pd
from currencycom.client import CandlesticksChartInervals, Client
from datetime import datetime

client = Client('hzUFvrYmvZVHw6OD', 'ZbLwL%SmbTf$tVf:38xzTxDmd-BirOw~')


def download_data(ticker):
       result = client.get_klines(ticker, interval=CandlesticksChartInervals('15m'))

       result = pd.DataFrame(data=result, columns=['date', 'open', 'high', 'low', 'close', 'volume'])
       result = result.set_index('date')
       result.index = pd.to_datetime(result.index/1000, unit='s')

       return result

print(download_data('BTC/USD'))



# print(datetime.fromtimestamp(1639808100))
# exchange_info = client.get_exchange_info()
# tradable_symbols = [x['symbol'] for x in exchange_info['symbols']]
# print(tradable_symbols)
