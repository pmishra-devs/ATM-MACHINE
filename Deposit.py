import utils
from utils import transactions 

def deposit ():
    amount = float(input("Enter amount to deposit in rupees "))
    global balance
    utils.balance = utils.balance + amount
    transactions.append(f"Deposited: ₹{amount}")
    print("Deposit successful!")
    
