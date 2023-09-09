from include import stock
from include import account

def main():
  # b = account.account("yes", 1000000000)
  a = stock.market("Yaboi LLC", 10000)
  a.add_stock("Yaboify", 1000)
  a.buy_stock("Yaboify", b, 2)

  
