import account

class market:
    def __init__(self, name: str, capital: int) -> None:
        self.name = name
        self.capital = capital
        self.stock = {
            str(self.stock): float(0),
        }

    def add_stock(self, stock_name: str, shares: int) -> None:
        self.stock[stock_name] = shares

    def get_stock_price(self, stock) -> float:
        return self.stock[stock]

    def calculate_stock_price(self, stock: str, amount: int) -> float:
        if not stock in self.stock:
            return False

        new_stock_price = round(amount/self.get_stock_price(stock), 2)
        
        return new_stock_price

    def buy_stock(self, stock: str, account: account.account, amount: int) -> bool:
        x = self.calculate_stock_price(stock, amount)
        self.stock[stock] = x
        account.withdraw(int(x))
        return True
