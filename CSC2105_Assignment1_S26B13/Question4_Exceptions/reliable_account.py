#Example of exception handling in Python
try:
    user_input = "five thousand"
    amount = float(user_input)  # Raises ValueError: invalid literal for float()
except ValueError:
    print("Handled: Non-numeric input received.")
else:
    print(f"Success: Processed amount UGX {amount:,.2f}")
finally:
    print("Cleanup: Operation attempt complete.")

class InsufficientFundsError(Exception):
    """Custom exception raised when a payment exceeds available balance."""
    pass

class StudentAccount:

    def __init__(self, name, registration_number, programme, balance, pin, dailylimit=100000.0):
        self.name = name
        self.registration_number = registration_number
        self._programme = programme
        self._dailylimit = dailylimit
        self._balance = balance
        self.__pin = pin

    def depositmoney(self, raw_amount):
        try:
            amount = float(raw_amount)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid input '{raw_amount}'. Deposit amount must be a valid number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")
        self._balance += amount
        print(f"[{self.name}] Deposited UGX {amount:,.2f}. New Balance: UGX {self._balance:,.2f}")

    def make_payment(self, raw_amount):
        try:
            amount = float(raw_amount)
        except (ValueError, TypeError):
            raise ValueError(f"Invalid input '{raw_amount}'. Payment amount must be a valid number.")
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero.")
        if amount > self._dailylimit:
            raise ValueError(f"Payment of UGX {amount:,.2f} exceeds daily limit of UGX {self._dailylimit:,.2f}.")
        if amount > self._balance:
            raise InsufficientFundsError(f"Insufficient funds! Requested UGX {amount:,.2f}, Available UGX {self._balance:,.2f}.")
        self._balance -= amount
        print(f"[{self.name}] Payment of UGX {amount:,.2f} successful. Remaining Balance: UGX {self._balance:,.2f}")



def transaction(account: StudentAccount, operation_type: str, raw_amount):
    print(f"\n--- Testing {operation_type}: '{raw_amount}' ---")
    try:
        if operation_type == "deposit":
            account.depositmoney(raw_amount)
        elif operation_type == "payment":
            account.make_payment(raw_amount)
    except (ValueError, InsufficientFundsError) as error:
        print(f"Error: {error}")
    else:
        print("Transaction completed.")
    finally:
        print(f"Balance: UGX {account._balance:,.2f}")


# Demonstration of Test Cases
account1 = StudentAccount("Jordan Feta", "S26B13/131", "BSIT", balance=50000.0, pin="1234")

#Deposit
transaction(account1  , "deposit", 20000.0)
#Invalid deposit
transaction(account1, "deposit", -5000.0)
#Payment
transaction(account1, "payment", 30000.0)
#Payment exceeding balance
transaction(account1, "payment", 100000.0)
#Numeric input not accepted
transaction(account1, "payment", "five thousand")