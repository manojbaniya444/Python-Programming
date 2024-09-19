from final import Person, Manager

bob = Person("Bob Smith")
tom = Manager("Tom Jones", 90000)

import shelve
db = shelve.open("./db/persondb")
for obj in (bob, tom):
    db[obj.name] = obj # using name as key when storing
    
# updating
tom = db["Tom Jones"]
tom.giveRaise(0.10)
db["Tom Jones"] = tom
    
db.close()