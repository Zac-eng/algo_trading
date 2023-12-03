class UserInfoGetter:
    def __init__(self, coincheck) -> None:
        self.coincheck = coincheck
    def getBalance(self):
        JPY = float(self.coincheck.fetch_balance()["info"]["jpy"])
        return JPY