from utils import transactions


def show_statement():
    print("\nTransaction Statement:")
    if not transactions:
        print("No transactions yet.")
    else:
        for t in transactions:
            print(t)