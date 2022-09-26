from abc import abstractmethod

from strategies.base_strategy import BaseStrategy


class BracketStrategy(BaseStrategy):

    @abstractmethod
    def _open_short_condition(self) -> bool:
        pass

    @abstractmethod
    def _open_long_condition(self) -> bool:
        pass

    # In a bracket strat, closing is done with stop loss or take profit -> no need to implement close conditions
    def _close_short_condition(self) -> bool:
        pass

    def _close_long_condition(self) -> bool:
        pass

    # Default calculation of stop price is using a stop loss in % and the actual market price
    def _get_long_stop_loss_price(self):
        return self.datas[0].close[0] * (1 - self.params.stop_loss / 100)

    def _get_short_stop_loss_price(self):
        return self.datas[0].close[0] * (1 + self.params.stop_loss / 100)

    # For take profit, we use a risk reward parameter, and it's a trivial calculation
    def _get_long_take_profit_price(self):
        stop_price = self._get_long_stop_loss_price()
        return self.datas[0].close[0] + (self.datas[0].close[0] - stop_price) * self.params.risk_reward

    def _get_short_take_profit_price(self):
        stop_price = self._get_short_stop_loss_price()
        return self.datas[0].close[0] - (stop_price - self.datas[0].close[0]) * self.params.risk_reward
