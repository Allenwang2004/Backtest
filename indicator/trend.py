import numpy as np
import pandas as pd
import sys
sys.path.append('..')
from ta_lib.trend import (
    MACD,
    ADXIndicator,
    AroonIndicator,
    CCIIndicator,
    DPOIndicator,
    EMAIndicator,
    IchimokuIndicator,
    KSTIndicator,
    MassIndex,
    PSARIndicator,
    SMAIndicator,
    STCIndicator,
    TRIXIndicator,
    VortexIndicator
)

def macd(close, window_slow=26, window_fast=12, window_sign=9):
    return MACD(close=pd.Series(close), window_slow=window_slow, window_fast=window_fast, window_sign=window_sign).macd().values

def adx(high, low, close, window=14):
    return ADXIndicator(high=pd.Series(high), low=pd.Series(low), close=pd.Series(close), window=window).adx().values

def aroon_up(high, low, window=25):
    return AroonIndicator(high=pd.Series(high), low=pd.Series(low), window=window).aroon_up().values

def aroon_down(high, low, window=25):
    return AroonIndicator(high=pd.Series(high), low=pd.Series(low), window=window).aroon_down().values

def cci(high, low, close, window=20, constant=0.015):
    return CCIIndicator(high=pd.Series(high), low=pd.Series(low), close=pd.Series(close), window=window, constant=constant).cci().values

def dpo(close, window=20):
    return DPOIndicator(close=pd.Series(close), window=window).dpo().values

def ema(close, window=14):
    return EMAIndicator(close=pd.Series(close), window=window).ema_indicator().values

def sma(close, window=14):
    return SMAIndicator(close=pd.Series(close), window=window).sma_indicator().values

def ichimoku_conversion_line(high, low, window1=9, window2=26, visual=False):
    return IchimokuIndicator(high=pd.Series(high), low=pd.Series(low), window1=window1, window2=window2, visual=visual).ichimoku_conversion_line().values

def ichimoku_base_line(high, low, window1=9, window2=26, visual=False):
    return IchimokuIndicator(high=pd.Series(high), low=pd.Series(low), window1=window1, window2=window2, visual=visual).ichimoku_base_line().values

def kst(close, roc1=10, roc2=15, roc3=20, roc4=30, window1=10, window2=10, window3=10, window4=15, nsig=9):
    return KSTIndicator(close=pd.Series(close), roc1=roc1, roc2=roc2, roc3=roc3, roc4=roc4,
                        window1=window1, window2=window2, window3=window3, window4=window4, nsig=nsig).kst().values

def mass_index(high, low, window_fast=9, window_slow=25):
    return MassIndex(high=pd.Series(high), low=pd.Series(low), window_fast=window_fast, window_slow=window_slow).mass_index().values

def psar_up(high, low, close, step=0.02, max_step=0.2):
    return PSARIndicator(high=pd.Series(high), low=pd.Series(low), close=pd.Series(close), step=step, max_step=max_step).psar_up().values

def psar_down(high, low, close, step=0.02, max_step=0.2):
    return PSARIndicator(high=pd.Series(high), low=pd.Series(low), close=pd.Series(close), step=step, max_step=max_step).psar_down().values

def stc(close, window_slow=50, window_fast=23, cycle=10, smooth1=3, smooth2=3):
    return STCIndicator(close=pd.Series(close), window_slow=window_slow, window_fast=window_fast,
                        cycle=cycle, smooth1=smooth1, smooth2=smooth2).stc().values

def trix(close, window=15):
    return TRIXIndicator(close=pd.Series(close), window=window).trix().values

def vortex_pos(high, low, close, window=14):
    return VortexIndicator(high=pd.Series(high), low=pd.Series(low), close=pd.Series(close), window=window).vortex_indicator_pos().values

def vortex_neg(high, low, close, window=14):
    return VortexIndicator(high=pd.Series(high), low=pd.Series(low), close=pd.Series(close), window=window).vortex_indicator_neg().values