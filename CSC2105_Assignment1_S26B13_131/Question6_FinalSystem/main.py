import os
TRANSACTION_FILE = "smart_campus_transactions.txt"


class InsufficientFundsError(Exception):
    pass

class StudentAccount:
    institution = "Uganda Christian University" 

    def __init__(self, name, reg_number, programme, balance, pin, daily_limit):
        # Encapsulation (Part c)
        self.name = name                       
        self.reg_number = reg_number           
        self._programme = programme           
        self._daily_limit = daily_limit       
        self.__balance = balance               
        self.__pin = pin   

    # Classic Getter & Setter
    def get_balance(self):
        return self.__balance
    def set_programme(self, programme_name):
        if isinstance(programme_name, str) and programme_name.strip():
            self._programme = programme_name.strip()

    # Property Getter & Setter
    @property
    def daily_limit(self):
        return self._daily_limit
    @daily_limit.setter
    def daily_limit(self, value: float):
        if isinstance(value, (int, float)) and value >= 0:
            self._daily_limit = float(value)
        else:
            raise ValueError(f"Daily limit cannot be negative: UGX {value}")

#Methods
#Deposit of money
    def deposit(self, raw_amount, service: str = "BANK") -> None:
        try:
            amount = float(raw_amount)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid deposit input '{raw_amount}'. Must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self.__balance += amount
        self._save_transaction("DEPOSIT", amount, service)
        print(f"[{self.name}] Deposited UGX {amount:,.2f}. Balance: UGX {self.__balance:,.2f}")

#Making payments
    def make_payment(self, raw_amount, service):
        try:
            amount = float(raw_amount)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid payment input '{raw_amount}'. Must be a number.")
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        if amount > self._daily_limit:
            raise ValueError(f"Payment UGX {amount:,.2f} exceeds daily limit of UGX {self._daily_limit:,.2f}.")
        if amount > self.__balance:
            raise InsufficientFundsError(f"Insufficient funds for {service}. Requested: UGX {amount:,.2f}, Available: UGX {self.__balance:,.2f}")
        self.__balance -= amount
        self._save_transaction("PAYMENT", amount, service)
        print(f"[{self.name}] Paid UGX {amount:,.2f} for {service}. Balance: UGX {self.__balance:,.2f}")

 #Saving of a transaction
    def _save_transaction(self, trans_type, amount, service):
        record = f"{self.reg_number} | {trans_type} | {amount:.0f} | {service.upper()} | {self.__balance:.0f}\n"
        with open(TRANSACTION_FILE, "a") as file:
            file.write(record)

#Display of summary
    def display_summary(self) -> None:
        print(f"[{self.reg_number}] {self.name} ({self._programme}) | Balance: UGX {self.__balance:,.2f}")

#View transaction history
def view_transaction_history() -> None:
    print("\n--- PERSISTED TRANSACTION HISTORY ---")
    try:
        with open(TRANSACTION_FILE, "r") as file:
            print(file.read().strip())
    except FileNotFoundError:
        print("No prior transaction log found.")


#Demonstartion of the working system
if __name__ == "__main__":
    if os.path.exists(TRANSACTION_FILE):
        os.remove(TRANSACTION_FILE)

    print("Campus System")

#Objects
student1 = StudentAccount("Feta Jordan", "S26B13/131", "BSIT", 300000, "1234", 50000)
student2 = StudentAccount("Jemimah Letasi.", "M25B13/021", "BVAD", 200000, "5678", 100000.0)
student3 = StudentAccount("George Wasike", "S25B13/021", "DIT", 50000, "9919", 20000)

#Deposit and payment of a service(printing)
student1.deposit(20000.0, "BANK")
student1.make_payment(3000.0, "PRINTING")

#Payment at Cafeteria
student2.make_payment(15000.0, "CAFETERIA")


print("Handling invalid transactions")
try:
    student3.make_payment(20000.0, "TUITION")
except (ValueError, InsufficientFundsError) as error:
    print(f"Caught Expected Failure: {error}")


    print("Account Summary")
student1.display_summary()
student2.display_summary()
student3.display_summary()

#Fileoutput
view_transaction_history()