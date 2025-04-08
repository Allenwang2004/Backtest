import numpy as np
import pandas as pd
import sys

sys.path.append('..')

from ta_lib.volume import (
    AccDistIndexIndicator,
    ChaikinMoneyFlowIndicator,
    EaseOfMovementIndicator,
    ForceIndexIndicator,
    MFIIndicator,
    NegativeVolumeIndexIndicator,
    OnBalanceVolumeIndicator,
    VolumePriceTrendIndicator,
    VolumeWeightedAveragePrice,
)

def acc_dist_index_indicator(high, low, close, volume, fillna=False):
    return AccDistIndexIndicator(high, low, close, volume, fillna).acc_dist_index()

def chaikin_money_flow_indicator(high, low, close, volume, window=20, fillna=False):
    return ChaikinMoneyFlowIndicator(high, low, close, volume, window, fillna).chaikin_money_flow()

def ease_of_movement_indicator(high, low, volume, window=14, fillna=False):
    return EaseOfMovementIndicator(high, low, volume, window, fillna).ease_of_movement()

def force_index_indicator(close, volume, window=13, fillna=False):
    return ForceIndexIndicator(close, volume, window, fillna).force_index()

def mfi_indicator(high, low, close, volume, window=14, fillna=False):
    return MFIIndicator(high, low, close, volume, window, fillna).money_flow_index()

def negative_volume_index_indicator(close, volume, fillna=False):
    return NegativeVolumeIndexIndicator(close, volume, fillna).negative_volume_index()

def on_balance_volume_indicator(close, volume, fillna=False):
    return OnBalanceVolumeIndicator(close, volume, fillna).on_balance_volume()

def volume_price_trend_indicator(close, volume, fillna=False, smoothing_factor=None, dropnans=False):
    return VolumePriceTrendIndicator(close, volume, fillna, smoothing_factor, dropnans).volume_price_trend()

def volume_weighted_average_price_indicator(high, low, close, volume, window=14, fillna=False):
    return VolumeWeightedAveragePrice(high, low, close, volume, window, fillna).volume_weighted_average_price()