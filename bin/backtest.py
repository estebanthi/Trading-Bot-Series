import backtrader as bt

from trading_bot import TradingBot
from timeframes import Timeframes
from data_sources.yfinance import Yfinance

from strategies import BracketStrategyExample


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

strategy = BracketStrategyExample
strategy_parameters = {
    'period_me1': 12, 'logging': True, 'stop_loss': 1, 'risk_reward': range(1, 5)
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