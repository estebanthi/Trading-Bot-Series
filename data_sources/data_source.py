from abc import ABC, abstractmethod
import pandas as pd
import datetime as dt
from timeframes import Timeframes


class DataSource(ABC):

    def get_data(self, backtest_parameters):
        start_date = backtest_parameters.get('start_date', dt.datetime(2019, 1, 1))
        end_date = backtest_parameters.get('end_date', dt.datetime(2020, 1, 1))
        timeframe = backtest_parameters.get('timeframe', Timeframes.d1)
        symbol = backtest_parameters.get('symbol', 'BTC-USD')

        print(f'Getting data for {symbol} from {start_date} to {end_date} with {timeframe.name} timeframe with {self.__class__.__name__} data source')
        return self._get_data(self._get_start_date(start_date), self._get_end_date(end_date), self._get_timeframe(timeframe), self._get_symbol(symbol))

    @abstractmethod
    def _get_data(self, start_date, end_date, timeframe, symbol) -> pd.DataFrame:
        pass

    def _get_start_date(self, start_date):
        return start_date

    def _get_end_date(self, end_date):
        return end_date

    def _get_timeframe(self, timeframe):
        return timeframe

    def _get_symbol(self, symbol):
        return symbol
