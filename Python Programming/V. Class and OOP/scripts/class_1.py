# allow this file to be imported from parent directory as well as run

class Person:
    def __init__(self, name, age, pay=0):
        self.name = name
        self.age = age
        self.pay = pay
        
if __name__ == "__main__": # when run for testing only
    # self test code run
    bob = Person("Bob", 20, 90000)
    sue = Person("Sue", 10, 10000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    