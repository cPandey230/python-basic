class BankAccount:
    Name = "Null"
    Occupation = "Null"
    Salary = 0
    Balance = 0

    def setup(self, name, occupation, salary, balance):
        self.Name = name
        self.Occupation = occupation
        self.Salary = salary
        self.Balance = balance

    def details(self):
        print(f"{self.Name} is a {self.Occupation} with a salary of Rs {self.Salary}")
        print(f"Your Balance is Rs: {self.Balance}\n")

    def deposit(self, depAmm):
        self.Balance += depAmm
        print(f"Rs {depAmm} deposited into your account.")
        print(f"Updated Balance: Rs {self.Balance}\n")

    def withdraw(self, wit_Amo):
        if wit_Amo <= self.Balance:
            self.Balance -= wit_Amo
            print(f"Rs {wit_Amo} has been withdrawn.")
        else:
            print("Insufficient Balance.")
        print(f"Balance after withdrawal: Rs {self.Balance}\n")

    def checkBalance(self):
        print(f"Your Balance is Rs: {self.Balance}\n")


def main():
    chandan = BankAccount()
    chandan.setup("Chandan", "Data Analyst", 50000, 2000000)
    chandan.details()
    chandan.deposit(20000)
    chandan.withdraw(10000)
    chandan.checkBalance()


main()
