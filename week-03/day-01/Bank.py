class Currency:
    def  __init__(self,number = 0,bName = "",vField = ""):
        self.number = number
        self.centre_bName = bName
        self.value_field = vField
    
    def getNumber(self):
        return self.number

    def setNumber(self,number):
        self.number = number
    
    def __str__(self):
        return f"{self.number} {self.value_field}"
    
class USADollar(Currency):
    def __init__(self,value):
        super().__init__(value,"Federal Reserve System","USD")

class HungarianForint(Currency):
    def __init__(self,value):
        super().__init__(value,"Hungarian National Bank","HUF")

class BankAccount(Currency):
    def __init__(self,pin,currency):
        self.pin = pin
        self.currency = currency
    
    def getNumber(self):
        return self.currency.getNumber()

    def deposit(self,cash):
        if cash >= 0:
            self.currency.setNumber(self.currency.getNumber() + cash)
        else:
            print("Invalid cash value")

    def withDraw(self,cash,pin):
        if pin == self.pin:
            if self.currency.getNumber() > cash:
                self.currency.setNumber(self.currency.getNumber() - cash)
            else:
                self.currency.setNumber(0)
        else:
            print("Invalid Pin")

    def __str__(self):
        return str(self.currency)

class Bank():
    def __init__(self,blist = []):
        self.account_list = blist
    
    def add_list(self,account):
        self.account_list.append(account)

    def getAllMoney(self):
        total_value = 0
        for account in self.account_list:
            total_value += account.getNumber()
        return total_value

curr1 = USADollar(30)
curr2 = HungarianForint(50)
#print(curr1.getNumber())
b1 = BankAccount(112233,curr1)
b2 = BankAccount(112233,curr2)
# print(str(b1))
# b1.deposit(30)
# print(str(b1))
# b1.withDraw(10,112233)
# print(str(b1))
b = Bank([b1])
b.add_list(b2)
print(b.getAllMoney())