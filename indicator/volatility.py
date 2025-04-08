import numpy as np
import pandas as pd
import sys

sys.path.append('..')

from ta_lib.volatility import (
    AverageTrueRange,
    BollingerBands,
    DonchianChannel,
    KeltnerChannel,
    UlcerIndex
)

# === Average True Range ===
def average_true_range_indicator(high, low, close, window=14):
    return AverageTrueRange(
        high=pd.Series(high),
        low=pd.Series(low),
        close=pd.Series(close),
        window=window
    ).average_true_range().values

# === Bollinger Bands ===
def bollinger_hband_indicator(close, window=20, window_dev=2):
    return BollingerBands(
        close=pd.Series(close),
        window=window,
        window_dev=window_dev
    ).bollinger_hband().values

def bollinger_lband_indicator(close, window=20, window_dev=2):
    return BollingerBands(
        close=pd.Series(close),
        window=window,
        window_dev=window_dev
    ).bollinger_lband().values

def bollinger_mavg_indicator(close, window=20):
    return BollingerBands(
        close=pd.Series(close),
        window=window
    ).bollinger_mavg().values

# === Donchian Channel ===
def donchian_hband_indicator(high, low, close, window=20):
    return DonchianChannel(
        high=pd.Series(high),
        low=pd.Series(low),
        close=pd.Series(close),
        window=window
    ).donchian_channel_hband().values

def donchian_lband_indicator(high, low, close, window=20):
    return DonchianChannel(
        high=pd.Series(high),
        low=pd.Series(low),
        close=pd.Series(close),
        window=window
    ).donchian_channel_lband().values

def donchian_mband_indicator(high, low, close, window=20):
    return DonchianChannel(
        high=pd.Series(high),
        low=pd.Series(low),
        close=pd.Series(close),
        window=window
    ).donchian_channel_mband().values

# === Keltner Channel ===
def keltner_hband_indicator(high, low, close, window=20):
    return KeltnerChannel(
        high=pd.Series(high),
        low=pd.Series(low),
        close=pd.Series(close),
        window=window
    ).keltner_channel_hband().values

def keltner_lband_indicator(high, low, close, window=20):
    return KeltnerChannel(
        high=pd.Series(high),
        low=pd.Series(low),
        close=pd.Series(close),
        window=window
    ).keltner_channel_lband().values

def keltner_mband_indicator(high, low, close, window=20):
    return KeltnerChannel(
        high=pd.Series(high),
        low=pd.Series(low),
        close=pd.Series(close),
        window=window
    ).keltner_channel_mband().values

# === Ulcer Index ===
def ulcer_index_indicator(close, window=14):
    return UlcerIndex(
        close=pd.Series(close),
        window=window
    ).ulcer_index().values