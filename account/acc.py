class Account:

    def __init__(self, filepath):
        self.filepath=filepath
        with open(filepath, 'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance=self.balance - amount

    def deposit(self,amount):
        self.balance=self.balance + amount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

#account=Account("account//balance.txt")
#print(account.balance)
#account.withdraw(100)
#account.deposit(200)
#print(account.balance)
#account.commit()

class Checking(Account):

    def __init__(self, filepath, fee):
        Account.__init__(self, filepath)
        self.fee=fee

    def transfer(self, amount):
        self.balance=self.balance - amount - self.fee


checking=Checking("account//balance.txt", 1)
#checking.deposit(10)
checking.transfer(110)
print(checking.balance)
checking.commit()

