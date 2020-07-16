class BankAcount:
  bank="KCB"
  
  def __init__(self, first_name, last_name):
    self.first_name=first_name
    self.last_name=last_name
    self.balance=0
    
  def account_name(self):
    name="{} account for {} {}".format(self.bank, self.first_name, self.last_name )
    return name
    
  def deposit (self, amount):
    self.balance += amount
    print("You have deposited {} to your account".format(amount)) 
    
  def get_balance(self):
    return "The balance for {} is {}".format (self.account_name(),self.balance)
    
  def withdraw(self, amount):
    self.balance -= amount
    print ("You have withdrawn {}  from your account".format(amount))
    if amount > self.balance:
      print ("Kindly update your account ")
      return
    elif:
      print ("Thanks for withdrawing")
      return
      
  def deposit_update(self,amount):
    self.balance += amount
    if amount > 0:
      print("You have deposited {} to your account".format(amount))
    else:
      print("Kindly top up {} to your account".format(amount))
            
    
acc1=BankAcount ("Betty", "Njambi")
acc2=BankAcount ("Hellen", "Ivy")



print()

acc1.deposit(100)
acc2.deposit(550)
acc1.deposit(467)
acc2.deposit(-100)
print()

acc1.withdraw(3000)
acc2.withdraw(150)

acc1.deposit_update(100)

acc2.deposit_update(-100)
print ()



print (acc1.get_balance()) 
print (acc2.get_balance())
print ()

print (acc1.get_balance())
print (acc2.get_balance())




    