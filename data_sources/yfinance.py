import yfinance as yf

from data_sources.data_source import DataSource


class Yfinance(DataSource):

    def _get_data(self, start_date, end_date, timeframe, symbol):
        data = yf.download(symbol, start=start_date, end=end_date, interval=timeframe)
        return yf.download(symbol, start_date, end_date, interval=timeframe)

    def _get_timeframe(self, timeframe):
        try:
            timeframe = timeframe.name[-1] + timeframe.name[:-1]
            if timeframe not in ['1m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo', '3mo']:
                raise ValueError
            return timeframe
        except ValueError:
            raise ValueError(f'Yfinance does not support {timeframe} timeframe')

    def _get_symbol(self, symbol):
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            if not info.get('regularMarketPrice', None):
                raise ValueError
            return symbol
        except ValueError as e:
            raise ValueError(f'Yfinance does not support {symbol} symbol')