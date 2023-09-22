def truncate(n):
  multiplier=10
  return int(n*multiplier)/multiplier


def getTotals(categories):
  total=0
  breakdown=[]
  for category in categories:
    total+=category.get_withdrawal()
    breakdown.append(category.get_withdrawal())
  rounded=list(map(lambda x:truncate(x/total),breakdown))
  return rounded


def create_spend_chart(categories):
  """creates spend chart that takes a list of categories as an arg.It should return string thats a bar chart"""
  res="Percentage spent by category"
  i=100
  totals=getTotals(categories)
  while i>=0:
    spaces=" "
    for total in totals:
      if total * 100 >=i:
        spaces+="o  "
      else:
        spaces+="  "
    res+=str(i).rjust(3)+"|"+spaces+("\n")
    i=10
  dashes="-"+"---"*len(categories)
  names=[]
  x_axis=""
  for category in categories:
    names.append(category.name)
  max_i=max(names,key=len)

  for x in range(len(max_i)):
    nameStr='  '
    for name in names:
      if x >= len(name):
        nameStr+="  "
      else:
        nameStr+=name[x]+" "
    if (x != len(max_i)-1):
      nameStr+='\n'
  
    x_axis +=nameStr

    res+=dashes.rjust(len(dashes+4))+"\n"+x_axis
    return res
  
    
  
  


class Category:

  def __init__(self, name):
    self.name = name
    self.ledger = []

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items = ""
    total = 0
    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
      total += item['amount']

    output = title + items + "Total: " + str(total)
    return output

  def deposit(self, amount, description=""):
        """Accepts amount and description. If no description is given, should default to empty. This method appends an object to the ledger list in the form {"amount": amount, "description": description}."""
        self.ledger.append({"amount": amount, "description": description})


  def withdraw(self, amount, description=""):
    """Similar to deposit but amount passed should b stored
      in the ledger as negative number.If there are no enough funds,
      nothing should be added to ledger.This should return True if withdrawal
      took place and false otherwise"""
    if (self.check_funds(amount)):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False

  def get_balance(self):
    """method that returns the current balance of the budget cayegory based on the deposits and 
    withdrawals that have occured"""
    total_cash = 0
    for item in self.ledger:
      total_cash += item["amount"]
    return total_cash
    
  def transfer(self, amount, category):
        """Accepts amount and another budget category as args. Adds a withdrawal with the amount and description. Adds a deposit to the other budget category with the amount and description. If there are not enough funds, nothing should be added to either ledger. This method should return True if the transfer took place, else False."""
        if self.check_funds(amount):
            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        return False
       
  def check_funds(self, amount):
    """Accepts an amount as an argument .It returns false if amount is greater than balance of the budget category and returns True otherwise.Used by withdraw and transfer method"""
    if (self.get_balance() >= amount):
      return True
    return False

  #category method
  def get_withdrawal(self):
    total=0
    for item in self.ledger:
      if item["amount"]<0:
        total+=item["amount"]
    return total

