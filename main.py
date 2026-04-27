
from utils import balance
from Withdrawmoney import withdraw
from Statement import show_statement
from Deposit import deposit
from Display import current_balance


def atm():
    while True:
        print("\n1. Display Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Statement")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            current_balance()
        elif choice == 2:
            deposit()
        elif choice == 3:
            withdraw()
        elif choice == 4:
            show_statement()
        elif choice == 5:
            print("Thank you for using ATM")
            break
        else:
            print("Invalid choice!")
atm()
