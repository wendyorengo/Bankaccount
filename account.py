from datetime import datetime
class Account:

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        
        self.phone_number = phone_number
        self.balance = 0
        self.deposits = []
        self.withdrawals = []
        self.loan_repayments =[]
        self.loan = 0
        self.pay_loan = 0
    
    def account_name(self):
        

        name = "{}  {} account for {}".format(
            self.first_name, self.last_name, self.bank)
        return name

    def get_formatted_time(self,time):
        return time.strftime("%H:%M%p , %d/%m/%Y")

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
            get_time = self.get_formatted_time(time)
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
            get_time = self.get_formatted_time(time)
            deposit = {
                "time": "time",
                "amount" : "amount"
            }
            print("Dear {} you have withdrawn {} at {} .Your current balance is {}".format(self.account_name(),amount,get_time,self.balance))

    
    def get_balance(self):
        time = datetime.now()
        get_time =  self.get_formatted_time(time)
        return "The balance for {} is {} at".format(self.account_name(), self.balance,get_time)

    def deposit_statements(self):
        for deposit in self.deposits:
            time = datetime.now()
            get_time =  self.get_formatted_time(time)
            print("{} at {}".format(deposit(),get_time))
        
    def withdrawal_statements(self):
        for withdraw in self.withdrawals:
            time = datetime.now()
            get_time =  self.get_formatted_time(time)
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
            get_time = self.get_formatted_time(time)
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
            repayment = {
                "time":"time",
                "amount":"amount"
            }
            self.loan_repayments.append(repayment)
            time = datetime.now()
            get_time = self.get_formatted_time(time)
            print("you have repaid your loan with this {}, your existing balance is {} at {}".format(amount,self.loan,get_time))
    
    def loan_repayment_statement(self):
        for repayment in self.loan_repayments:
            time = repayment['time']
            amount = repayment['amount']
            get_time = self.get_formatted_time(time)
            statement = "you repaid {} on {}".format(amount,get_time)
            print(statement)

class BankAccount(Account):
    def __init__(self,first_name,last_name,phone_number,bank):
        self.bank = bank
        super().__init__(first_name,last_name,phone_number)

class MobileMoney(Account):
    def __init__(self,first_name,last_name,phone_number,service_provider):

        self.service_provider = service_provider
        self.airtime=[]
        super().__init__(first_name,last_name,phone_number)

    def buy_airtime(self,amount):
        try:
            amount + 1
        except TypeError:
            print("The amount should be in figures")
            return
        
        if amount > self.balance:
            print("you do not have enough balance. Your balance is {}".format(self.balance))
        
        else:
            self.balance -= amount
            time = datetime.now()
            airtime = {
                "time":"time",
                "airtime":"amount"
            }
            self.airtime.append(airtime)
            print("you have bought airtime worth {} shillings on {}. Your  balance is {}".format(amount,get_formatted_time(time),self.balance))

    def send_money(self,amount):
        try:
            amount + 10
        except TypeError:
            print("The amount should be in digits")

        if amount > self.balance:
            print("you have insufficient funds to conduct the transaction")
        else:
            self.balance -= amount
            time = datetime.now()
            print("you have sent {} on {}. Your account balance is {}".format(amount,get_formatted_time(time),self.balance))

    def receive_money(self,amount):
        try:
            amount + 10
        except TypeError:
            print("The amount should be in digits")

        if amount > self.balance:
            time = datetime.now()
            print("you have received {} on {}. Your balance is {}".format(amount,get_formatted_time(time),self.balance))

    def paybill(self,amount):
        try:
            amount + 10
        except TypeError:
            print("The amount should be in digits")

        if amount > self.balance:
            print("your balance cannot pay the above bill")

        else:
            amount <= self.balance
            time = datetime.now()
            print("you have paid a bill of {} on {}. Your account balance is {}".format(amount,get_formatted_time,self.balance))

        





    
