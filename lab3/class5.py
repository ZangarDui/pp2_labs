class BankAccount:  
    def __init__(self, owner, balance=0):  
        self.owner = owner  
        self.balance = balance  

    def deposit(self, amount):  
        if amount > 0:  
            self.balance += amount  
            print(f"{amount} теңге депозитке салынды. Қазіргі баланс: {self.balance}")
        else:
            print("Депозитке салу үшін дұрыс мән енгізіңіз!")

    def withdraw(self, amount):  
        if amount > 0:  
            if amount <= self.balance:  
                self.balance -= amount  
                print(f"{amount} теңге есепшоттан алынды. Қазіргі баланс: {self.balance}")
            else:
                print("Қалаған соманы алу үшін жеткілікті баланс жоқ!")
        else:
            print("Шығарылатын сома оң болу керек!")


account = BankAccount("Ali", 1000)  
account.deposit(500)  
account.withdraw(200)  
account.deposit(-50)
account.withdraw
