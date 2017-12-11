class Account:
  def __init__(self, name, balance, min_balance):
    self.name = name
    self.balance = balance
    self.min_balance = min_balance

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    if self.balance - amount >= self.min_balance:
      self.balance -= amount
    else:
      print("sorry not enough money")

  def statement(self):
    print("account balance: ${}".format(self.balance))


class Current(Account):
  def __init__(self, name, balance):
    super().__init__(name, balance, minimum_balance = -1000)