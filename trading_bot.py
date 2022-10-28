import backtrader as bt
import datetime as dt

from timeframes import Timeframes


class TradingBot:

    def backtest(self, strategy, backtest_parameters, data_source, sizer=bt.sizers.FixedSize, strategy_parameters=None,
                 sizer_parameters=None, analyzers=None):
        cerebro = bt.Cerebro()

        data = data_source.get_data(backtest_parameters)
        datafeed = bt.feeds.PandasData(dataname=data)
        cerebro.adddata(datafeed)

        initial_cash = backtest_parameters.get('initial_cash', 10000)
        commission = backtest_parameters.get('commission', 0.001)
        slippage = backtest_parameters.get('slippage', 0.001)

        cerebro.broker.setcash(initial_cash)
        cerebro.broker.setcommission(commission=commission)
        cerebro.broker.set_slippage_perc(slippage)

        cerebro.adddata(datafeed)

        self.configure_cerebro(cerebro, strategy, strategy_parameters, sizer, sizer_parameters, analyzers, live=False)

        results = cerebro.run(maxcpus=1)
        return results

    def live(self, strategy, live_parameters, store, sizer=bt.sizers.FixedSize, strategy_parameters=None,
             sizer_parameters=None, analyzers=None):
        data = store.get_data(dataname=live_parameters.get('dataname'))
        broker = store.getbroker()

        cerebro = bt.Cerebro()
        cerebro.adddata(data)
        cerebro.setbroker(broker)

        self.configure_cerebro(cerebro, strategy, strategy_parameters, sizer, sizer_parameters, analyzers, live=True)

        result = cerebro.run()
        return result

    @staticmethod
    def configure_cerebro(cerebro, strategy, strategy_parameters, sizer, sizer_parameters, analyzers, live=False):
        if not strategy_parameters:
            strategy_parameters = {}
        if live:
            cerebro.addstrategy(strategy, **strategy_parameters)
        else:
            cerebro.optstrategy(strategy, **strategy_parameters)

        if not sizer_parameters:
            sizer_parameters = {}
        cerebro.addsizer(sizer, **sizer_parameters)

        if analyzers:
            for analyzer in analyzers:
                cerebro.addanalyzer(analyzer)