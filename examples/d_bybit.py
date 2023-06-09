from cryptofeed import FeedHandler
from cryptofeed.backends.aggregate import OHLCV
from cryptofeed.callback import Callback
from cryptofeed.defines import TRADES
from cryptofeed.exchanges import Coinbase


async def ohlcv(data=None):
    print(data)


def main():
    f = FeedHandler()
    f.add_feed(Coinbase(pairs=['BTC-USD', 'ETH-USD', 'BCH-USD'], channels=[TRADES], callbacks={TRADES: OHLCV(Callback(ohlcv), window=300)}))

    f.run()


if __name__ == '__main__':
    main()
