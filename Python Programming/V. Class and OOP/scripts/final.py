"""
Record and process information about people.
Run this file directly to test its classes.
"""

from tool import AttrDisplay

class Person(AttrDisplay):
    """
    create and process person records
    """
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
        
    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))

class Manager(Person):
    """
    a customized Person with special requirements
    """
    def __init__(self, name, pay):
        Person.__init__(self, name, "mgr", pay)
        
    def giveRaise(self, percent, bonus=0.10):
        Person.giveRaise(self, percent + bonus)
        
if __name__ == "__main__":
    bob = Person("Bob Smith")
    sue = Person("Sue Jones", job="dev", pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(0.10)
    print(sue)
    tom = Manager("Tom Jones", 50000)
    tom.giveRaise(0.10)
    print(tom.lastName())
    print(tom)
    print(tom.gatherAttributes())
    
## Output:
# Person: job=None, name=Bob Smith, pay=0
# Person: job=dev, name=Sue Jones, pay=100000
# Smith Jones
# Person: job=dev, name=Sue Jones, pay=110000
# Jones
# Manager: job=mgr, name=Tom Jones, pay=60000
# job=mgr, name=Tom Jones, pay=60000