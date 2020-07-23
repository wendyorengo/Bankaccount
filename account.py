class BankAccount:

    def __init__(self, first_name, last_name, bank, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.bank = bank
        self.phone_number = phone_number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan = 0
        self.pay_loan = 0
    
    def account_name(self):
        name = "{} account for {} {}".format(
            self.bank, self.first_name, self.last_name)
        return name
    
    def deposit(self, amount):
        deposit = self.deposits.append(amount)
        if amount <= 0:
            print("You have to deposit a higher amount")
        else:
            self.balance += amount
            print("You have deposited {} to {}".format(amount, self.account_name()))
            
    def withdraw(self, amount):
        withdraw = self.withdrawals.append(amount)
        if amount <= 0:
            print("You have to withdraw a positive amount")
        elif amount > self.balance:
            print("You don't have enough balance to make the transition")
        else:
            self.balance -= amount
            print("You have withdrawn {} from {}".format(amount, self.account_name()))
        
    
    def get_balance(self):
        return "The balance for {} is {}".format(self.account_name(), self.balance)

    def deposit_statements(self):
        for deposit in self.deposits:
            print(deposit)
        
        

    def withdrawal_statements(self):
        for withdraw in self.withdrawals:
            print(withdraw)
        

    def request_loan(self,amount):
        if amount <= 0:
            print("you cannot withdraw a negative value")
        else:
            self.loan = amount
            print("you have been granted a loan of shillings {}".format(amount))   
        

    def repay_loan(self,amount):
        if amount <= 0:
            print("you cannot repay a negative amount.Kindly top up")
        elif self.loan == 0:
            print("you do not have an existing loan")
        elif amount > self.loan:
            print("your loan is {}, please enter a amount that is less or equal to your loan".format(self.loan))
        else:
            self.loan -= amount
            self.repay = self.loan - amount
            print("you have repaid your loan with this {}, your existing balance is {}".format(amount,self.loan))
            



    
