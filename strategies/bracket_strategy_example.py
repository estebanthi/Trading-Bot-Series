from backtrader.indicators import MACD as MACD
from backtrader.indicators import CrossOver as CrossOver
from backtrader.indicators import ExponentialMovingAverage as EMA

from strategies.bracket_strategy import BracketStrategy


# This is a test strategy, to help you understand how to build one
class BracketStrategyExample(BracketStrategy):

    # First, you define some parameters
    params = (
        ('period_me1', 12),
        ('period_me2', 26),
        ('period_signal', 9),
        ('trend_ema_period', 100),
        ('movav', EMA),
    )

    # Then, you initialize indicators
    def _init_indicators(self):
        self.macd = MACD(period_me1=self.p.period_me1, period_me2=self.p.period_me2, period_signal=self.p.period_signal,
                         movav=self.p.movav)
        self.ema = EMA(period=self.p.trend_ema_period)
        self.cross = CrossOver(self.macd.macd, self.macd.signal)

    # Finally, you implement your open conditions
    # Closing is done with stop loss or take profit
    def _open_long_condition(self) -> bool:
        if self.ema[0] < self.datas[0].close[0] and self.cross[0] == 1:
            return True
        return False

    def _open_short_condition(self) -> bool:
        if self.ema[0] > self.datas[0].close[0] and self.cross[0] == -1:
            return True
        return False
