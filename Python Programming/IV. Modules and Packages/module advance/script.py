from module import *

# print(a, _b) # error because _b is not accessible using importing *

from module import _b
print(_b) # in this way we can get b value here

from all import *
# print(name, _address) Here we will get error because _address and name is not accessible using importing * because we have specified __all__ in all.py

# but we can access contact
# print(contact) 


from all import name, _address, contact
print(name, _address, contact) # in this way we can get name and __address value here