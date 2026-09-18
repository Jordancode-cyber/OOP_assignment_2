#Class with defined attributes and methods for a student account
class StudentAccount:

    def __init__(self, name, registration_number, programme, balance, pin, dailylimit):
        self.name = name
        self.registration_number = registration_number
        self._programme = programme
        self._dailylimit = dailylimit
        self.__balance = balance
        self.__pin = pin

#Method to deposit money into the account       
    def depositmoney(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit successful. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

#Method to make a payment from the account
    def makepayment(self, amount, pin):
        if pin == self.__pin:
            if amount <= self.__balance and amount <= self._dailylimit:
                self.__balance -= amount
                print(f"Payment successful. New balance: {self.__balance}")
            elif amount > self.__balance:
                print("Insufficient balance for this payment.")
            else:
                print("Payment exceeds daily limit.")
        else:
            print("Incorrect PIN. Payment failed.")

#Method to display account summary
    def accountsummary(self):
        print(f"Account summary for {self.name}:")
        print(f"Registration Number: {self.registration_number}")
        print(f"Programme: {self._programme}")
        print(f"Current Balance: {self.__balance}")

#Student accounts
account1 = StudentAccount("Feta Jordan", "S26B13/131", "BSIT", 300000, "1234", 50000)
account2 = StudentAccount("Jemimah Letasi.", "M25B13/021", "BVAD", 200000, "5678", 100000.0)
account3 = StudentAccount("George Wasike", "S25B13/021", "DIT", 50000, "9919", 20000)

print("Demonstration example:")
account1.depositmoney(20000)                  
account1.makepayment(30000, "1234")     

account1.accountsummary()
account2.accountsummary()
account3.accountsummary()

print("Encapsulation Demonstration:")
print(f"Name: {account1.name}") 
#No restrictions attached so name can be accessed directly
print(f"Programme: {account1._programme}")
#This will print however it is not recommended to access protected attributes directly

print(f"Balance: {account1.__balance}")
#This will raise an AttributeError since balance is private and cannot be accessed directly

print("Name mangling:")
print(f"Balance: {getattr(account1, '_StudentAccount__balance')}")
#When an attribute starts with double underscores (__attribute), Python automatically
#renames it internally to _ClassName__attribute (e.g., _StudentAccount__balance).
#This is done to prevent access to private attributes from outside the class.