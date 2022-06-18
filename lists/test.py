class Category:
  
  funds = 0
    
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    data = []
    for i in range(len(self.ledger)):
      if len(self.ledger[i]["description"]) > 23:
        limited = slice(0, 23)
        self.ledger[i]["description"] = self.ledger[i]["description"][limited]
      
      data.append("{:<23}{:>7}\n".format(self.ledger[i]["description"], format(float(self.ledger[i]["amount"]),'.2f')))
    return f"*************{self.name}*************\n"+''.join(data) + "Total: " + str(self.funds)
    
  def check_funds(self, amount):
    return True if amount <= self.funds else False
  
  def deposit(self, amount, description=""):
    self.amount = amount
    self.description = description
    self.ledger.append(
      {"amount":self.amount, "description":self.description})
    self.funds += self.amount

  def withdraw(self, amount,description=""):
    self.whdrw_amount = amount
    self.description = description
    self.check = self.check_funds(self.whdrw_amount)
    if self.check:
      self.funds -= self.whdrw_amount
      self.ledger.append(
        {"amount":-abs(self.whdrw_amount),
        "description": self.description}
      )
      return True
    else:
      return False

  
  def get_balance(self):
    return self.funds

  def transfer(self, amount, destination):
  
    self.transfer_amount = amount
    self.destination = destination
    if self.funds >= self.transfer_amount:
      self.ledger.append(
        {"amount":-abs(self.transfer_amount),"description":"Transfer to {}".format(self.destination.name)})
      self.description = "Transfer from {}".format(self.name)
      self.destination.deposit(self.transfer_amount,self.description)
      self.funds -= self.transfer_amount
      return True
    else:
      return False
    

food = Category("Food")
entertainment = Category("Enterteinment")
food.deposit(900, "deposit")
food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
food.transfer(20, entertainment)
# print(test.ledger)
# print(test.funds)
# print(test2.ledger)
# print(test2.funds)
print(food)

def create_spend_chart(categories):
  pass