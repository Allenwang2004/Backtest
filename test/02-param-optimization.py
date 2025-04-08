import datetime
import pandas as pd
import sys
sys.path.append('..')
from indicator.momentum import rsi_indicator
from backtesting.backtesting import Backtest
from backtesting.backtesting import Strategy
from backtesting.lib import crossover

GOOG = pd.read_csv('/Users/coconut/Yuanta/backtest/data/GOOG.csv', index_col=0, parse_dates=True)

class RsiOscillator(Strategy):
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

if __name__ == '__main__':
    bt = Backtest(GOOG, RsiOscillator, cash=10_000, commission=.002)
    stats = bt.optimize(
        upper_bound=range(55, 85, 5),
        lower_bound=range(10, 45, 5),
        rsi_window=range(10, 30, 2),
        maximize="Sharpe Ratio",
        constraint=lambda param: param.upper_bound > param.lower_bound
    )
    bt.plot()
