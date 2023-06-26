

# Create a parent Account class which is going to be inherited by the CurrentAccount class

class AccountGeneral:
    def __init__(self, balance):
        self.balance = balance

    def printbalance(self):
        print("The balance of the account is:",self.balance)



# Quick Exercise - 1:
# Create a class for a current account,
# which will have 2 objects account1 and account2
#   Define 2 methods sum1 and average which will sum
#   and print the average of the two attributes of each object
#   Also create 2 attributes for account 1 named a and b
#   and assign 100 and 500 to each
# Create 2 attributes for account 2 named a and b
# and assign 200 and 400 to each


class CurrentAccount(AccountGeneral):
    def __init__(self, a, b, balance):
        super().__init__(balance)
        self.a = a
        self.b = b

    def sum1(self):
        return self.a + self.b

    def average1(self):
        return (self.a + self.b) / 2


# Create account1 with attributes a=100 and b=500
account1 = CurrentAccount(100, 500, 0)
# Create account2 with attributes a=200 and b=400
account2 = CurrentAccount(200, 400, -100)
# Calculate the sum and average for account1
sum_account1 = account1.sum1()
average_account1 = account1.average1()
# Calculate the sum and average for account2
sum_account2 = account2.sum1()
average_account2 = account2.average1()

# Print the results
print("Account1 - Sum:", sum_account1)
print("Account1 - Average:", average_account1)
print("Account2 - Sum:", sum_account2)
print("Account2 - Average:", average_account2)
account1.printbalance()
account2.printbalance()

# Quick Exercise - 2:
# create a class named Person which has:
# attributes firstname and lastname and a method open_account()
# which prints: <person name> can talk
# and use a constructor for creating instancevariables/objectvariables/attributes

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def open_account(self):
        return print(f'{self.firstname} {self.lastname}',"opens now a bank account")

person1 = Person("Paul","Clientovich")
person2 = Person("Peter","Accountir")
person1.open_account()
person2.open_account()


# Q: Create a vehicle class that takes in 3 params (name,mileage,capacity)
# Create a Bus child class that inherits from the Vehicle class.
# The default fare charge of any vehicle is
# seating capacity * 100. so total fare is: capacity * 100
# if the mileage is greater than 100 than total fare
# increases by 10% and if it's greater than 500 then
# it increases by 50%
# Print the total fare for the object

class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def farecharge(self):
        fare = self.capacity * 100
        if self.mileage > 100:
            fare *= 1.1
        if self.mileage > 500:
            fare *= 1.5
        return fare

class Bus(Vehicle):
    pass

# Create a Vehicle instance
vehicle = Vehicle("Car", 200, 4)
print("Fare charge for the vehicle:", vehicle.farecharge())

# Create a Bus instance
bus = Bus("School Bus", 600, 40)
print("Fare charge for the bus:", bus.farecharge())


# Q: Create a parent class of Human which takes in name,age and pref
# create another class of Employee that will inherit from the Human class
# and will also take in name , age , pref and occupation. use the super function to get
# the name and age from the human class
# add a __str__ method in the Employee class that will print all the details

class Human:
    def __init__(self, name, age, pref):
        self.name = name
        self.age = age
        self.pref = pref

    def printname(self):
        print(self.name)
    
class Employee(Human):
    def __init__(self, name, age, pref, occupation):
        super().__init__(name, age, pref)
        self.occupation = occupation

    def __str__(self) -> str:
        return f"Name: {self.name}\nAge: {self.age}\nPreference: {self.pref}\nOccupation: {self.occupation}"
    
employee = Employee("John Doe", 34, "office", "Software Engineer")
print(employee)


# Q: Make 2 classes cash_inflow and cash_outflow. 
# Cash_inflow will have a method to add cash to account and cash_outflow will
# have a method to remove cash from an account.
# Then make a account class which will inherit from both cash_inflow and cash_outflow
# and will have a display_total_transactions method that will display 
# all the transaction that have been made so far and a display_current_wealth 
# that will show how much money is there in the account right now. 
# Use multiple inheritance to solve this problem.

class Cash_inflow:
    def __init__(self):
        self.transactions = []

    def add_cash(self, amount):
        self.transactions.append(amount)


class Cash_outflow:
    def __init__(self):
        self.transactions = []

    def remove_cash(self, amount):
        self.transactions.append(-amount)


class Account(Cash_inflow, Cash_outflow):
    def display_total_transactions(self):
        print("Transactions:")
        for transaction in self.transactions:
            if transaction > 0:
                print(f"Cash inflow: {transaction}")
            else:
                print(f"Cash outflow: {abs(transaction)}")

    def display_current_wealth(self):
        total_cash = sum(self.transactions)
        print(f"Current wealth: {total_cash}")


# Example usage
account = Account()

account.add_cash(1000)
account.add_cash(2000)
account.remove_cash(500)
account.add_cash(1500)

account.display_total_transactions()
account.display_current_wealth()

    
# Q: Create a class with 2 methods add and average and call them
# sequentially using method chaining
# add will take in a list of numbers and calculate their total and
# average will calculate the average of the total

class MathOperations:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, numbers):
        self.total += sum(numbers)
        self.count += len(numbers)
        return self

    def average(self):
        if self.count == 0:
            return 0
        return self.total / self.count

# Example usage
numbers = [1, 2, 3, 4, 5]

result = MathOperations().add(numbers).average()
print(f"Average: {result}")

