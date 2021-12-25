import tvDatafeed
from tvDatafeed import Interval


def RSI(data, window=8, adjust=False):
    delta = data.diff(1).dropna()
    loss = delta.copy()
    gains = delta.copy()

    gains[gains<0] = 0
    loss[loss>0] = 0

    gain_ewm = gains.ewm(com=window-1, adjust=adjust).mean()
    loss_ewm = abs(loss.ewm(com=window-1, adjust=adjust).mean())

    RS = gain_ewm / loss_ewm
    RSI = 100 - 100/(1 + RS)
    
    return RSI

def get_rsi(asset='BTCUSD', interval=Interval.in_15_minute, exchange='CURRENCYCOM'):
    r = tvDatafeed.TvDatafeed()
    r = r.get_hist(asset, exchange, interval, n_bars=1000)
    r['RSI'] = RSI(r['close'])
    rsi = r.RSI[-1].round(2)
    return rsi
