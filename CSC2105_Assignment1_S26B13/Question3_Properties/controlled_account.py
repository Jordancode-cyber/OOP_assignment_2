class StudentAccount:

    def __init__(self, name, registration_number, programme, balance, pin, dailylimit):
        self.name = name
        self.registration_number = registration_number
        self._programme = programme
        self._dailylimit = dailylimit
        self._balance = balance
        self.__pin = pin
#Classic getter
    def get_balance(self):
        return self._balance
#Classic setter
    def set_programme(self, programme):
        if isinstance(programme, str) and programme.strip():
            self._programme = programme
        else:
            raise ValueError("Programme must be a non-empty string.")

#@property(setter and getter)
    @property
    def daily_limit(self):
        return self._dailylimit
    
    @daily_limit.setter
    def daily_limit(self, dailylimit):
        if dailylimit < 0:
            raise ValueError("Daily limit cannot be negative.")
        self._dailylimit = dailylimit

    @property
    def account_status(self):
        return "Active" if self._balance > 0 else "Inactive"

account1 = StudentAccount("Feta Jordan", "S26B13/131", "BSIT", 300000, "1234", 50000)

#Part a
print(f"Current Balance: UGX {account1.get_balance():,.2f}")

#Part b1
account1.set_programme("Software Engineering")

# Part d
account1.daily_limit = 75000.0                   
print(f"Daily Limit: UGX {account1.daily_limit:,.2f}")
# Invalid property 
try:
    account1.daily_limit = -10000.0
except ValueError as e:
    print(f"Invalid daily limit rejected: {e}")
print(f"Daily Limit preserved: UGX {account1.daily_limit:,.2f}")

#Read only property 
print(f"Status: {account1.account_status}")
try:
    setattr(account1, "account_status", "blocked")
except AttributeError as e:
    print(f"Attempt to modify read-only property failed: {e}")

