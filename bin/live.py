import backtrader as bt
from backtrader.stores.oandastore import OandaStore
from ccxtbt import CCXTStore
import time

from trading_bot import TradingBot
from strategies.bracket_strategy_example import BracketStrategyExample


oanda_token = 'YOUR_OANDA_TOKEN'
oanda_account = 'YOUR_OANDA_ACCOUNT'

binance_api_key = 'YOUR_BINANCE_API_KEY'
binance_api_secret = 'YOUR_BINANCE_API_SECRET'

timezone = 'America/New_York'
sandbox = True

store1 = OandaStore(
    token=oanda_token,
    account=oanda_account,
    practice=sandbox,
    timezone=timezone,
)
store2 = CCXTStore(
    exchange='binance',
    currency='USD',
    config={
        'apiKey': binance_api_key,
        'secret': binance_api_secret,
        'nonce': lambda: str(int(time.time() * 1000)),
        'enableRateLimit': True,
    },
    sandbox=sandbox,
    timezone=timezone,
)

bot = TradingBot()

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

live_parameters = {
    'dataname': 'EUR_USD',
}
bot.live(strategy, store1, strategy_parameters=strategy_parameters, sizer=sizer,
         sizer_parameters=sizer_parameters, analyzers=analyzers)
