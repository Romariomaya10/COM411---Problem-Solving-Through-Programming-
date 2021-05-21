class Person:

  def __init__(self, fn, ln):
    self.first_name = fn
    self.last_name = ln
    self.address = None

  def set_address(self, address):
    self.address = address

  def __str__(self):
    return f"{self.first_name} {self.last_name}"

class IndividualAccount:

  def __init__(self, sort_code, account_number, owner):
    self.sort_code = sort_code
    self.account_number = account_number
    if type(owner) is Person:
      self.owner = owner
    else:
      self.owner = None
    self.balance = 0

  def get_account_data(self):
    print(f"The account beelongs to {self.owner}. The account number is {self.account_number}. the balancce is {self.balance}")

  def pay_in(self, money):
    self.balance += money

  def withdraw(self, money):
    self.balance -= money

class SharedAcccount:

  def __init__(self,sort_code, account_number):
    self.sort_code = sort_code
    self.account_number = account_number
    self.owners = []
    self.balance = 0

  def pay_in(self, money):
    self.balance += money

  def withdraw(self, money):
    self.balance -= money

  def get_account_data(self):
    full_owners = ""
    for person in self.owners:
      full_owners + person + " "
    print(f"This shared account belongs to {full_owners}. The account number is {self.account_number}. The balance is {self.balance}.")

p1 = Person ("Piotr", "Bednorz")
p2 = Person ("Ovidiu", "Borze")
p3 = Person ("Daniel", "Grab")
p4 = Person ("Geza","Smith")

acc1 = IndividualAccount("10-23-56", "120103232", p2)
acc2 = IndividualAccount("45-63-74", "956632125", p3)
acc3 = IndividualAccount("452163578", " 65-35-15", p4)


acc1.get_account_data()
acc2.get_account_data()
acc3.get_account_data()

acc1.pay_in(80)
acc2.withdraw(2030)
acc3.pay_in(1360)

acc1.get_account_data()
acc2.get_account_data()
acc3.get_account_data()