import backtrader as bt

from trading_bot import TradingBot
from timeframes import Timeframes
from data_sources.yfinance import Yfinance


bot = TradingBot()
data_source = Yfinance()

backtest_parameters = {
    'start_date': '2010-01-01',
    'end_date': '2022-01-01',
    'timeframe': Timeframes.d1,
    'symbol': 'AAPL',
    'initial_cash': 10000,
    'commission': 0.001,
    'slippage': 0.001
}

strategy = bt.strategies.MA_CrossOver
strategy_parameters = {
    'fast': range(10, 15),
}

sizer = bt.sizers.PercentSizer
sizer_parameters = {
    'percents': 99
}

analyzers = [
    bt.analyzers.TradeAnalyzer
    ]

results = bot.backtest(strategy, backtest_parameters, data_source, strategy_parameters=strategy_parameters, sizer=sizer,
                       sizer_parameters=sizer_parameters, analyzers=analyzers)
for result in results:
    print(f"Net profit: {result[0].analyzers.tradeanalyzer.get_analysis()['pnl']['net']['total']}")
