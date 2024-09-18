import module_a
import module_b
import module_c
# from module_b import spam
# from module_b import sum
# from module import * # can do this also

# importing module_a gives this script access to eberything defined by the top level code in the file module_a.py

print("The top level module run first.")

module_a.spam("Hello from module_a")
result = module_b.sum(1, 2)
print("The sum result is of module b: ", result)

print(module_b.spam) # from module_b variable
module_b.spam = 9
from module_b import spam # this will not update the value of spam in module_b because second import dont rerun the modules code, they just fetch the already created module object from python internal modules table.
print("New spam value: ", spam) # from module_b variable

print("The top level module run last.") # this will run last because the module_a, module_b and module_c are imported and their top level code is executed first.