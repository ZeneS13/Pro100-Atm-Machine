import random
class Atm:
    def __init__(self,balance,password,uniqueCode):
        self.balance=balance
        self.password=password
        self.uniqueCode=uniqueCode
        
    
    def checkBalance(self):
        print('-'*72)
        print("the balance in acc",self.uniqueCode," is: $",self.balance)
            
    def withdrawMoney(self):
        print('-'*72)
        print("Whitdrawal happening below")
        amount=int(input("Enter amount that you want to withdraw: "))
        self.balance=self.balance-amount
        print("Your new balance is: $", self.balance)
            

    def depositMoney(self):
        print('-'*72)
        print("Desposit happening below")
        amountAdded=int(input("Enter amount that you want to put in account: "))
        self.balance=self.balance+amountAdded
        print("Your new balance is: $", self.balance)
        
    def changePassword(self):
        print('-'*72)
        print("Password change booth")
        self.password=input("Enter new password of 8 characters: ")
        print("Password changed successfully")
        print("new password is: ",self.password)
        
        
unique=random.randint(1,9999)        
person1=Atm(1000,"123r5678",unique)

print("Welcome at the atm machine")
print('-'*72)


balanceCheck=input("Do you want to check your balance? Put Y if Yes AND press the enter key if not: ")
print('-'*72)
if balanceCheck=="Y":
    person1.checkBalance()
        
withdraw=input("Do you want to withdraw money? Put Y if Yes AND press the enter key if not: ")
print('-'*72)
if withdraw=="Y":
    person1.withdrawMoney()
        
deposit=input("Do you want to deposit money? Put Y if Yes AND press the enter key if not: ")
print('-'*72)
if deposit=="Y":
    person1.depositMoney()
        
password=input("Do you want to change password? Put Y if Yes AND press the enter key if not: ")
print('-'*72)
if password=="Y":
    person1.changePassword()
        
print("Thanks for coming")        
       
        
        
    
