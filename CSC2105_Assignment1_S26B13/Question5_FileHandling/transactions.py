import os
FILE_NAME = "transactions.txt"

def log_transaction(reg_num, trans_type, amount, service, balance):
    record = f"{reg_num} | {trans_type.upper()} | {amount:.0f} | {service.upper()} | {balance:.0f}\n"
    with open(FILE_NAME, "a") as file:
        file.write(record)

#Transaction History
def read_transactions() -> None:
    print("Transaction History")
    try:
        with open(FILE_NAME, "r") as file:
            content = file.read().strip()
            if content:
                print(content)
            else:
                print("No transactions recorded yet.")
    except FileNotFoundError:
        print("Notice: 'transactions.txt' does not exist yet. No past transactions to show.")

#Example
if __name__ == "__main__":
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
    print("File")
#Reads transactions
    read_transactions() 
#Logs transactions
    log_transaction("M25B13/021", "PAYMENT", 5000, "CAFETERIA", 25000)
    log_transaction("S26B13/001", "DEPOSIT", 20000, "BANK", 45000)
#Reads previous transactions
    read_transactions()