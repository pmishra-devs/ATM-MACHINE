import utils
from utils import transactions, balance


def withdraw(): 
    global balance
    print(f"Current Balance: ₹{utils.balance}")
    amount = float(input("Enter amount to withdraw: ₹"))
    if amount >= utils.balance:
        print("Insufficient balance!")
    else:
        utils.balance -= amount
        transactions.append(f"Withdrawn: ₹{amount}")
        print("Withdrawal successful!")
    