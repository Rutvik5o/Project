class BankAccount:


    def __init__(self,name,balance=0):

        self.account_holder=name

        self.balance=balance

    
    def deposit(self,amount):

        self.balance += amount

        print(f"=>Deposited {amount} in your account.")

    def withdrawn(self,amount):

        if amount>self.balance:

            print("Your Account In Not Have Sufficient Amount")

        else:

            self.balance -= amount

            print("Sucessfully Withdrawn")

        
    def __str__(self):

        return f"Account Holder Name=> {self.account_holder}\nBalance=>{self.balance}"
    

Obj=BankAccount("ABC",4000)

print(Obj)

Obj.deposit(10000)

Obj.withdrawn(5000)

print(Obj)

Obj.withdrawn(10000)
    