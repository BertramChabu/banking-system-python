class Customer:
    def __init__(self,customer_id,name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.accounts = []

    def returnCustomer():
        return "Customer({self.customer_id}, {sefl.name},{self.address})"

class Account:
    def __init__(self, account_number, account_type, balance=0):
        self.account_numnber = account_number
        self.account_type = account_type
        self.balance = balance


    def returnAccount(self):
        return "Customer: ", self.account_numnber ," ",self.account_type , " ", self.balance



class Bank:
    def __init__(self, bank_name, address):
        self.bank_name = bank_name
        self.address = address
        self.customers = []
        self.accounts = []


    def add_customers(self,customer_id,name, address):
        new_customer = Customer(customer_id,name,address)
        self.customers.append(new_customer)
        print("Customer " , self.customer[name] , " added successfully")
        return new_customer

    def open_account(self,customerId, accountNumber, account_type, initial_deposit = 0):
        for c in self.customers:
            if c.customer_id == self.customerId:
                account =  Account(accountNumber,account_type, initial_deposit)
                self.accounts.append(account)
                print("Account successfully opened")
            else:
                print("Customer ID not found")

    def deposit(self,account_no, amount):
        for a in self.accounts:
            if a.account_number == account_no:
                a.initial_deposit += amount
                print("Amount successfully deposited, Your new amount is: ", a.intial_deposit)
            else:
                print("Account not found")

    def withdraw(self,account_no, amount):
        for w in self.accounts:
            if w.account_number == account_no:
                if w.intital_deposit > amount:
                    w.intitial_deposit -=amount
                    print("You have successfully withdrawn: " , amount)
                    print("Your new bank Account balance is: ", w.intitial_deposit)
                else:
                    print("Cannot withdraw from bank Account you have low funds")
            else:
                print("Account not Found")

    def transfer(from_account, to_account):
        



