import sys
sys.path.append('..')
from backtesting.backtesting import Strategy, Backtest

from backtesting.lib import crossover
import talib
class RSI(Strategy):
    
    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    def init(self):
        self.rsi = self.I(talib.RSI, self.data.Close, self.rsi_window)
    
    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()

        elif crossover(self.lower_bound, self.rsi):
            self.position.close()
            self.buy()