# import talib
import os
from dotenv import load_dotenv
import ccxt
# import pandas as pd
# from time import sleep
# import sys
from UserInfoGetter import UserInfoGetter

load_dotenv()
API_KEY = os.environ['API_KEY']
SECRET_KEY = os.environ['SECRET_KEY']

symbol = "BTC/JPY"
amount = 0.005

coincheck = ccxt.coincheck({'apiKey':API_KEY,'secret':SECRET_KEY})

def main():
    my_info_getter = UserInfoGetter(coincheck)
    jpy_balance = my_info_getter.getBalance()
    print(jpy_balance)
    return 0

if __name__ == "__main__":
    main()
