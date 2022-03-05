from crypto_scraper import CryptoCurrency
import time
import os

if __name__ == '__main__':
    while True:
        symbol1 = CryptoCurrency(symbol="btcusd")
        symbol2 = CryptoCurrency(symbol="ethusd")
        symbol3 = CryptoCurrency(symbol="bnbusdt")
        symbol4 = CryptoCurrency(symbol="xrpusdt")
        symbol5 = CryptoCurrency(symbol="lunausdt")
        symbol6 = CryptoCurrency(symbol="adausdt")
        symbol7 = CryptoCurrency(symbol="solusdt")
        symbol8 = CryptoCurrency(symbol="dotusdt")
        symbol9 = CryptoCurrency(symbol="dogeusdt")
        symbol10 = CryptoCurrency(symbol="maticusdt")
        symbol11 = CryptoCurrency(symbol="atomusdt")
        symbol12 = CryptoCurrency(symbol="uniusdt")
        symbol13 = CryptoCurrency(symbol="fttusdt")
        symbol14 = CryptoCurrency(symbol="xmrusdt")

        CryptoCurrency.show_prices()
        time.sleep(3)
        CryptoCurrency.clean_prices()
        os.system("cls")