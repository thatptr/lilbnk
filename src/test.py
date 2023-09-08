from include import stock

def main():
  a = stock.market("Yaboi LLC", 10000)
  a.add_stock("Yaboify", 2)

  print(a.get_stock_price("Yaboify"))
  
