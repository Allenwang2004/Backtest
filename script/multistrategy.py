import sys
import pandas as pd
sys.path.append('..')

from backtesting.backtesting import MultiStrategy

from indicator.momentum import rsi_indicator
from indicator.trend import macd
from backtesting.backtesting import Backtest
from backtesting.backtesting import Strategy
from backtesting.lib import crossover

GOOG = pd.read_csv('/Users/coconut/Yuanta/backtest/data/GOOG.csv', index_col=0, parse_dates=True)

class RsiOscillator1(Strategy):
    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    def init(self):
        self.rsi = self.I(
            rsi_indicator,
            self.data.Close, self.rsi_window
        )

    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()

class RsiOscillator2(Strategy):
    upper_bound = 70
    lower_bound = 30
    rsi_window = 7

    def init(self):
        self.rsi = self.I(
            rsi_indicator,
            self.data.Close, self.rsi_window
        )

    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()

class MacdStrategy(Strategy):
    window_slow = 26
    window_fast = 12
    window_sign = 9

    def init(self):
        self.macd = self.I(macd, self.data.Close, self.window_slow, self.window_fast, self.window_sign)

    def next(self):
        if crossover(self.macd, 0):
            self.buy()
        elif crossover(0, self.macd):
            self.position.close()

if __name__ == '__main__':
    ms = MultiStrategy(GOOG, strategy_bucket=[RsiOscillator1, RsiOscillator2,MacdStrategy], cash=30000)
    ms.run()
    ms.plot() 
    # RsiOscillator1_op = {
    # 'upper_bound': range(55, 85, 5),
    # 'lower_bound': range(10, 45, 5),
    # 'rsi_window': range(10, 30, 2),
    # 'maximize': "Sharpe Ratio",
    # 'constraint': lambda p: p.upper_bound > p.lower_bound,
    # 'random_state': 42
    # }
    # RsiOscillator2_op = {
    # 'upper_bound': range(55, 85, 5),
    # 'lower_bound': range(10, 45, 5),
    # 'rsi_window': range(10, 30, 2),
    # 'maximize': "Sharpe Ratio",
    # 'constraint': lambda p: p.upper_bound > p.lower_bound,
    # 'random_state': 42
    # }
    # stat = ms.optimize(
    #     RsiOscillator1_op,
    #     RsiOscillator2_op
    # )
    #print(stat)
