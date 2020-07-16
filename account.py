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

    def deposit_statements(self,amount):
        
        statement_deposit = " The deposit statements for {} {} is {}".format(self.first_name, self.last_name,amount)
        return statement_deposit

    def withdrawal_statements(self,amount):
        statement_withdraw = " The withdrawal statements for {} {} is {}".format(self.first_name, self.last_name,amount)
        return statement_withdraw

    def give_loan(self,amount):
        loan = "Dear {} {} you have received a loan of {} shillings".format(self.first_name, self.last_name,amount) 
        return loan

    def pay_loan(self,amount):
        if amount >= 1:
            self.repay = self.loan - amount
            print("You have paid {} shillings of the exixting loan".format(amount))



    
