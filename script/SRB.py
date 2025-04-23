import datetime
import pandas as pd
import numpy as np
import sys
sys.path.append('..')
from backtesting.backtesting import Backtest
from backtesting.backtesting import Strategy
from backtesting.lib import crossover

data= pd.read_csv('/Users/coconut/Backtest/data/BTCUSDT_futures_4h_from_20210101.csv', index_col=0, parse_dates=True)

# 計算 MACD 指標
def MACD(close, fast_period=12, slow_period=26, signal_period=9):
    close = pd.Series(close)
    exp1 = close.ewm(span=fast_period, adjust=False).mean()
    exp2 = close.ewm(span=slow_period, adjust=False).mean()
    macd = exp1 - exp2
    signal = macd.ewm(span=signal_period, adjust=False).mean()
    return macd, signal

# MACD 策略類別
class MACDStrategy(Strategy):
    def init(self):
        close = self.data.Close
        self.macd, self.signal = self.I(
            lambda x: MACD(x)[0], close
        ), self.I(
            lambda x: MACD(x)[1], close
        )

    def next(self):
        if crossover(self.macd, self.signal):
            self.position.close()
            self.buy()
        elif crossover(self.signal, self.macd):
            self.position.close()
            self.sell()

# 執行回測
bt = Backtest(data, MACDStrategy, cash=1000000, commission=.002)
stats = bt.run()
print(stats)