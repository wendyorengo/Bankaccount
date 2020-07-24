from datetime import datetime
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
        

        name = "{}  {} account for {}".format(
            self.first_name, self.last_name, self.bank)
        return name
    
    def deposit(self, amount):
        try:

            amount + 1
        except TypeError:

            print("The amount should be digits")
            return
        if amount <= 0:
            try:
                amount + 1
            except TypeError:
                print("The amount should be in digits")
                return
            deposit=self.deposits.append(amount)
       
            print("You have to deposit a higher amount")

        else:
            self.balance += amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p , %d/%m/%Y")
            deposit = {
                "time": "time",
                "amount" : "amount"
            }
            print("Dear {} ,you have deposited {} at {}.Your current balance is {}".format(self.account_name(),amount,get_time,self.balance))

    def withdraw(self,amount):
        try:
            amount + 1
        except TypeError:
            print("The amount should be in digits")
            return
        if amount <= 0:
            

            deposit=self.withdrawals.append(deposit)
            print("You have to withdraw a positive amount")
        elif amount > self.balance:
            print("You don't have enough balance to make the transition")
        else:
            self.balance -= amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p ,  %d/%m/%Y")
            deposit = {
                "time": "time",
                "amount" : "amount"
            }
            print("Dear {} you have withdrawn {} at {} .Your current balance is {}".format(self.account_name(),amount,get_time,self.balance))

    
    def get_balance(self):
        time = datetime.now()
        get_time = time.strftime("%H:%M%p ,  %d/%m/%Y")
        return "The balance for {} is {} at".format(self.account_name(), self.balance,get_time)

    def deposit_statements(self):
        for deposit in self.deposits:
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  , %d/%m/%Y")
            print("{} at {}".format(deposit(),get_time))
        
    def withdrawal_statements(self):
        for withdraw in self.withdrawals:
            time = datetime.now()
            get_time = time.strftime("%H:%M%p , ++ %d/%m/%Y")
            print("{} at {}".format(withdraw(),get_time))

    def request_loan(self,amount):
        try:
            amount + 1
        except TypeError:
            print("The amount should be digits")
            return
        if amount <= 0:

            try:
                amount + 1
            except TypeError:
                print("The amount should be digits")
                return

        
            print("you cannot withdraw a negative value")
        else:
            self.loan = amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            print("you have been granted a loan of shillings {} at {}".format(amount,get_time))   
        

    def repay_loan(self,amount):
        try:
            amount + 1
        except TypeError:
            print("The amount should be digits")
            return
        if amount <= 0:
            print("you cannot repay a negative amount.Kindly top up")
        elif self.loan == 0:
            print("you do not have an existing loan")
        elif amount > self.loan:
            print("your loan is {}, please enter a amount that is less or equal to your loan".format(self.loan))
        else:
            self.loan -= amount
            self.repay = self.loan - amount
            time = datetime.now()
            get_time = time.strftime("%H:%M%p  %d/%m/%Y")
            print("you have repaid your loan with this {}, your existing balance is {} at {}".format(amount,self.loan,get_time))
            



    
