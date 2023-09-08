class bank:
    def __init__(self, name: str, capital: int) -> None:
        self.name = name

        if capital < 10_000_00:
            self.capital = 10_000_00

        self.capital = capital

    def remove_capital(self, amount: int) -> bool:
        if self.capital < 0:
            return False

        self.capital -= amount
        return True

    def add_capital(self, amount: int) -> None:
        self.capital += amount

    def get_capital(self) -> int:
        return self.capital

    def get_name(self) -> str:
        return self.name
