import numpy as np
import pandas as pd
import sys
sys.path.append('..')
from ta_lib.momentum import (
    RSIIndicator,
    TSIIndicator,
    UltimateOscillator,
    StochasticOscillator,
    KAMAIndicator,
    ROCIndicator,
    AwesomeOscillatorIndicator,
    WilliamsRIndicator
)

# 可用於 self.I 的指標函數包裝

def rsi_indicator(close, window):
    return RSIIndicator(close=pd.Series(close), window=window).rsi().values

def tsi_indicator(close, window_slow=25, window_fast=13):
    return TSIIndicator(close=pd.Series(close), window_slow=window_slow, window_fast=window_fast).tsi().values

def ultimate_oscillator_indicator(high, low, close, w1=7, w2=14, w3=28):
    return UltimateOscillator(high=pd.Series(high), low=pd.Series(low), close=pd.Series(close), window1=w1, window2=w2, window3=w3).ultimate_oscillator().values

def stochastic_k_indicator(high, low, close, window=14):
    return StochasticOscillator(high=pd.Series(high), low=pd.Series(low), close=pd.Series(close), window=window).stoch().values

def stochastic_d_indicator(high, low, close, window=14, smooth=3):
    return StochasticOscillator(high=pd.Series(high), low=pd.Series(low), close=pd.Series(close), window=window, smooth_window=smooth).stoch_signal().values

def kama_indicator(close, window=10, pow1=2, pow2=30):
    return KAMAIndicator(close=pd.Series(close), window=window, pow1=pow1, pow2=pow2).kama().values

def roc_indicator(close, window=12):
    return ROCIndicator(close=pd.Series(close), window=window).roc().values

def ao_indicator(high, low, w1=5, w2=34):
    return AwesomeOscillatorIndicator(high=pd.Series(high), low=pd.Series(low), window1=w1, window2=w2).awesome_oscillator().values

def williams_r_indicator(high, low, close, lbp=14):
    return WilliamsRIndicator(high=pd.Series(high), low=pd.Series(low), close=pd.Series(close), lbp=lbp).williams_r().values