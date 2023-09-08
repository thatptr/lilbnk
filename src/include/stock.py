class market:
    def __init__(self, name: str, capital: int) -> None:
        self.name = name
        self.capital = capital
        self.stock = {
            str(self.stock): 0,
        }

    def add_stock(self, stock_name: str, shares: int) -> None:
        self.stock[stock_name] = shares

    def get_stock_price(self, stock) -> int:
        return self.stock[stock]
