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


class AdxStrategy(Strategy):
    adx_window = 14

    def init(self):
        self.adx = self.I(adx, self.data.High, self.data.Low, self.data.Close, self.adx_window)

    def next(self):
        if self.adx[-1] > 25:
            self.buy()
        elif self.adx[-1] < 20:
            self.position.close()


class AroonStrategy(Strategy):
    window = 25

    def init(self):
        self.aroon_up = self.I(aroon_up, self.data.High, self.data.Low, self.window)
        self.aroon_down = self.I(aroon_down, self.data.High, self.data.Low, self.window)

    def next(self):
        if crossover(self.aroon_up, self.aroon_down):
            self.buy()
        elif crossover(self.aroon_down, self.aroon_up):
            self.position.close()


class CciStrategy(Strategy):
    window = 20

    def init(self):
        self.cci = self.I(cci, self.data.High, self.data.Low, self.data.Close, self.window)

    def next(self):
        if self.cci[-1] > 100:
            self.buy()
        elif self.cci[-1] < -100:
            self.position.close()


class DpoStrategy(Strategy):
    window = 20

    def init(self):
        self.dpo = self.I(dpo, self.data.Close, self.window)

    def next(self):
        if crossover(self.dpo, 0):
            self.buy()
        elif crossover(0, self.dpo):
            self.position.close()


class EmaStrategy(Strategy):
    window = 14

    def init(self):
        self.ema = self.I(ema, self.data.Close, self.window)

    def next(self):
        if crossover(self.data.Close, self.ema):
            self.buy()
        elif crossover(self.ema, self.data.Close):
            self.position.close()


class SmaStrategy(Strategy):
    window = 14

    def init(self):
        self.sma = self.I(sma, self.data.Close, self.window)

    def next(self):
        if crossover(self.data.Close, self.sma):
            self.buy()
        elif crossover(self.sma, self.data.Close):
            self.position.close()


class IchimokuStrategy(Strategy):
    window1 = 9
    window2 = 26

    def init(self):
        self.conv = self.I(ichimoku_conversion_line, self.data.High, self.data.Low, self.window1, self.window2)
        self.base = self.I(ichimoku_base_line, self.data.High, self.data.Low, self.window1, self.window2)

    def next(self):
        if crossover(self.conv, self.base):
            self.buy()
        elif crossover(self.base, self.conv):
            self.position.close()


class KstStrategy(Strategy):
    def init(self):
        self.kst = self.I(kst, self.data.Close)

    def next(self):
        if crossover(self.kst, 0):
            self.buy()
        elif crossover(0, self.kst):
            self.position.close()

class MassIndexStrategy(Strategy):
    window_fast = 9
    window_slow = 25

    def init(self):
        self.mi = self.I(mass_index, self.data.High, self.data.Low, self.window_fast, self.window_slow)

    def next(self):
        if self.mi[-1] > 27:
            self.buy()
        elif self.mi[-1] < 26.5:
            self.position.close()

class PsarStrategy(Strategy):
    step = 0.02
    max_step = 0.2

    def init(self):
        self.psar_up = self.I(psar_up, self.data.High, self.data.Low, self.data.Close, self.step, self.max_step)
        self.psar_down = self.I(psar_down, self.data.High, self.data.Low, self.data.Close, self.step, self.max_step)

    def next(self):
        if self.psar_down[-1] < self.data.Close[-1]:
            self.buy()
        elif self.psar_up[-1] > self.data.Close[-1]:
            self.position.close()

class StcStrategy(Strategy):
    def init(self):
        self.stc = self.I(stc, self.data.Close)

    def next(self):
        if crossover(self.stc, 25):
            self.buy()
        elif crossover(75, self.stc):
            self.position.close()

class TrixStrategy(Strategy):
    window = 15

    def init(self):
        self.trix = self.I(trix, self.data.Close, self.window)

    def next(self):
        if crossover(self.trix, 0):
            self.buy()
        elif crossover(0, self.trix):
            self.position.close()

class VortexStrategy(Strategy):
    window = 14

    def init(self):
        self.vortex_pos = self.I(vortex_pos, self.data.High, self.data.Low, self.data.Close, self.window)
        self.vortex_neg = self.I(vortex_neg, self.data.High, self.data.Low, self.data.Close, self.window)

    def next(self):
        if crossover(self.vortex_pos, self.vortex_neg):
            self.buy()
        elif crossover(self.vortex_neg, self.vortex_pos):
            self.position.close()
