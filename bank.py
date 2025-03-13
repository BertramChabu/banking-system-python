import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk  # Modern Tkinter styling

# Customer Class
class Customer:
    def __init__(self, customer_id, name, address):
        self.customer_id = customer_id
        self.name = name
        self.address = address
        self.accounts = []

# Account Class
class Account:
    def __init__(self, account_number, account_type, balance=0):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance

# Bank Class
class Bank:
    def __init__(self, bank_name, address):
        self.bank_name = bank_name
        self.address = address
        self.customers = []
        self.accounts = {}

    def add_customer(self, customer_id, name, address):
        new_customer = Customer(customer_id, name, address)
        self.customers.append(new_customer)
        return new_customer

    def open_account(self, customer_id, account_number, account_type, initial_deposit=0):
        customer = next((c for c in self.customers if c.customer_id == customer_id), None)
        if customer:
            account = Account(account_number, account_type, initial_deposit)
            self.accounts[account_number] = account
            customer.accounts.append(account)
            return account
        return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount
            return self.accounts[account_number].balance
        return None

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and self.accounts[account_number].balance >= amount:
            self.accounts[account_number].balance -= amount
            return self.accounts[account_number].balance
        return None

    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account].balance >= amount:
                self.accounts[from_account].balance -= amount
                self.accounts[to_account].balance += amount
                return True
        return False

# GUI Class
class BankGUI:
    def __init__(self, root, bank):
        self.bank = bank
        self.root = root
        self.root.title("Banking System")
        self.root.geometry("500x650")
        self.root.resizable(False, False)
        self.style = ttk.Style(theme="darkly")  # Modern theme

        # Title Label
        ttk.Label(root, text="🏦 Python Bank", font=("Arial", 20, "bold")).pack(pady=10)

        # Notebook (Tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True)

        # Creating Frames for Different Tabs
        self.create_add_customer_tab()
        self.create_open_account_tab()
        self.create_transaction_tab()

    def create_add_customer_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Add Customer")

        ttk.Label(frame, text="Customer ID").pack(pady=2)
        self.customer_id_entry = ttk.Entry(frame)
        self.customer_id_entry.pack(pady=2)

        ttk.Label(frame, text="Name").pack(pady=2)
        self.customer_name_entry = ttk.Entry(frame)
        self.customer_name_entry.pack(pady=2)

        ttk.Label(frame, text="Address").pack(pady=2)
        self.customer_address_entry = ttk.Entry(frame)
        self.customer_address_entry.pack(pady=2)

        ttk.Button(frame, text="Add Customer", command=self.add_customer, bootstyle="success").pack(pady=10)

    def create_open_account_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Open Account")

        ttk.Label(frame, text="Customer ID").pack(pady=2)
        self.acc_customer_id_entry = ttk.Entry(frame)
        self.acc_customer_id_entry.pack(pady=2)

        ttk.Label(frame, text="Account Number").pack(pady=2)
        self.account_number_entry = ttk.Entry(frame)
        self.account_number_entry.pack(pady=2)

        ttk.Label(frame, text="Account Type").pack(pady=2)
        self.account_type_entry = ttk.Entry(frame)
        self.account_type_entry.pack(pady=2)

        ttk.Label(frame, text="Initial Deposit").pack(pady=2)
        self.initial_deposit_entry = ttk.Entry(frame)
        self.initial_deposit_entry.pack(pady=2)

        ttk.Button(frame, text="Open Account", command=self.open_account, bootstyle="primary").pack(pady=10)

    def create_transaction_tab(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Transactions")

        ttk.Label(frame, text="Account Number").pack(pady=2)
        self.transaction_account_entry = ttk.Entry(frame)
        self.transaction_account_entry.pack(pady=2)

        ttk.Label(frame, text="Amount").pack(pady=2)
        self.transaction_amount_entry = ttk.Entry(frame)
        self.transaction_amount_entry.pack(pady=2)

        ttk.Button(frame, text="Deposit", command=self.deposit_money, bootstyle="success").pack(pady=5)
        ttk.Button(frame, text="Withdraw", command=self.withdraw_money, bootstyle="warning").pack(pady=5)

    def add_customer(self):
        customer_id = self.customer_id_entry.get()
        name = self.customer_name_entry.get()
        address = self.customer_address_entry.get()
        customer = self.bank.add_customer(customer_id, name, address)
        if customer:
            messagebox.showinfo("Success", f"Customer {name} added successfully!")
        else:
            messagebox.showerror("Error", "Customer could not be added!")

    def open_account(self):
        customer_id = self.acc_customer_id_entry.get()
        account_number = self.account_number_entry.get()
        account_type = self.account_type_entry.get()
        initial_deposit = float(self.initial_deposit_entry.get())

        account = self.bank.open_account(customer_id, account_number, account_type, initial_deposit)
        if account:
            messagebox.showinfo("Success", "Account opened successfully!")
        else:
            messagebox.showerror("Error", "Customer ID not found!")

    def deposit_money(self):
        account_number = self.transaction_account_entry.get()
        amount = float(self.transaction_amount_entry.get())

        new_balance = self.bank.deposit(account_number, amount)
        if new_balance is not None:
            messagebox.showinfo("Success", f"Deposit successful! New balance: {new_balance}")
        else:
            messagebox.showerror("Error", "Account not found!")

    def withdraw_money(self):
        account_number = self.transaction_account_entry.get()
        amount = float(self.transaction_amount_entry.get())

        new_balance = self.bank.withdraw(account_number, amount)
        if new_balance is not None:
            messagebox.showinfo("Success", f"Withdrawal successful! New balance: {new_balance}")
        else:
            messagebox.showerror("Error", "Insufficient funds or account not found!")

# Running the GUI
bank = Bank("Python Bank", "123 Bank Street")
root = ttk.Window(themename="darkly")  # Set dark theme
app = BankGUI(root, bank)
root.mainloop()
