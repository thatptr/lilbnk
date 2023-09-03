from enum import Enum
from bank import *

class acc_type(Enum):
  debit = 1
  credit = 1
  saving = 1

class account:
  def __init__(self, name: str, age: int, acc_type: acc_type, bank: bank, amount: int) -> None:
    self.name = name
    self.age = age
    self.type = acc_type
    self.bank = bank
    self.amount = amount

  def get_name(self) -> str:
    return self.name
  
  def get_acc_type(self) -> acc_type:
    return self.type

  def withdraw(self, amount: int) -> bool:
    self.bank.add_capital(10)

    if (acc_type == acc_type.saving):
      return False
    
    if (self.amount < amount):
      if (acc_type == acc_type.debit):
        self.amount -= amount
        self.amount -= amount / 10
        self.bank.add_capital(int(amount / 10))
        return True
      
      if (acc_type == acc_type.credit):
        self.amount -= amount
        return True
      
    self.amount -= amount
    return True
  
  def deposit(self, amount: int) -> None:
    self.amount += amount

def transfer(get: account, to:account, amount: int):
  get.withdraw(amount)
  to.deposit(amount)
