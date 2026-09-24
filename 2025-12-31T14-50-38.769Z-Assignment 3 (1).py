"""Question 1: Create a class named Car with the attributes brand, model, and year. 
Include a constructor to initialize these values and a method display_info() to print all the car details. 
Then create an object of the Car class and display its details."""


class car:
    def __init__(self, brand ,modle , year):
        self.brand=brand
        self.modle=modle
        self.year=year
    def display_info(self):
        print("car brand:",self.brand)
        print("car modle:",self.modle)
        print("Manufacture Year:", self.year)

# Creating an object of Car class
my_car=car("BMW","X6 M Competition SUV",2020)
my_car.display_info()
        


'''Question 2: Create three classes Animal, Mammal, and Dog where Animal has a method eat(),
Mammal inherits from Animal and has a method walk(), and Dog inherits from Mammal and has a method bark(). 
Create an object of Dog and demonstrate all three methods. 
Also, create a class Calculator with an add() method that can take either two or three parameters,
 and then create a subclass Advanced Calculator that overrides the add() method to add any number of parameters using 
 variable-length arguments. Demonstrate both functionalities.'''

class Animal:
    def eat(self):
        print("animal can eat")

class Mammal(Animal):
    def walk(self):
        print("mammal can walk")
    
class Dog(Mammal):
    def bark(self):
        print('dog can bark')


# Creating Dog object
d = Dog()
print("Demonstrating Multilevel Inheritance:")
d.eat()     
d.walk()    
d.bark() 

class calculator:
    def add(self,a,b,c=None):
        if c is not None:
            return a+b+c
        else:
            return a+b
        
class advanced_calculator(calculator):
    def add(self,*number):  #Why we use *numbers-->Because we want the AdvancedCalculator add() method to accept any number of 
                            #arguments, not just 2 or 3.
        total=0
        for i in number:
            total+=i
        return total

c=calculator()
ac=advanced_calculator()

print("\nDemonstrating Calculator Functionality:")
print("Calculator add (2 numbers):", c.add(10, 20))
print("Calculator add (3 numbers):", c.add(10, 20, 30))

print("\nAdvanced Calculator (any number of values):")
print("Add 2 numbers:", ac.add(5, 10))
print("Add 4 numbers:", ac.add(1, 2, 3, 4))
print("Add 6 numbers:", ac.add(10, 20, 30, 40, 50, 60))


""""Question 3: Create a class BankAccount with a private attribute balance and 
provide methods deposit() and withdraw() to modify the balance safely 
so that the balance cannot be accessed directly. 
Then create two subclasses SavingsAccount and CurrentAccount, 
each having a method account_type() that prints its respective account type. 
Demonstrate polymorphism by calling account_type() from different account objects.
"""



class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance    

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance



class SavingsAccount(BankAccount):
    def account_type(self):
        print("This is a Savings Account")


class CurrentAccount(BankAccount):
    def account_type(self):
        print("This is a Current Account")




print("Encapsulation Demo:")
acc = BankAccount(1000)
acc.deposit(500)
acc.withdraw(300)



print("Current Balance:", acc.get_balance())


print("\nPolymorphism Demo:")
savings = SavingsAccount()
current = CurrentAccount()

for account in (savings, current):
    account.account_type()




      