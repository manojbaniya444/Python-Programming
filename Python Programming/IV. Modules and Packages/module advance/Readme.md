## Advance Module Topics
- Data Hiding
- __future__ module
- __name__ variable
- sys.path changes
- listing tools
- importing modules by name string
- many more

## Module Design Concepts
We have to think about which functions go in which modules, module communication mechanism and so on.

- We are always in a module in python
Even interactive prompt code really goes in a built in module called __main__

- Minimize module coupling: global variables
Like function module works best if they are written to be closed boxes. They should be independent of global variables used within other module as possible. The only thing a module should share with the outside are the tools it uses and the tools it define

- Maximize module cohesion: unified purpose
If all the components of a module share a general purpose we are less likely to depend on external name.

- Modules should rarely change other modules variables

## Data Hiding in Modules
How to prevent global variable of module to prevent from changing by other modules? Is there encapsulation in Python Programming language?

We can use prefix names with a single underscore `**(_x)**` to prevent them from being copied out when client import a module name with a from * statement.

```python
# unders.py
a, _b, c, _d, e = 1,2,3,4,5

from unders import *
a, c
# error loading _b

import unders
unders._b # this can get
```

## using __all___
__all__ has precedence over _x. We can specify those items which we dont want to share in a list 

__all__ = ['a','_b'] # dont share a and _b

But here also another type of import will get all the values even if we try to protect it. Still we can use either technique.

## Enabling Future Language Features: __future__
The __future__ module in python is used to enable new language features that are not compatible with the current interpreter version. These features are typically slated for inclusion in future versions of python but can be tested and used in the current version by importing the __future__ module.

## Mixed Usuage Modes: __name__ and __main__
Import a file as a module and run it as a standalone program.

Each module has a built in attribute called __name__ which python creates and assigns automataically as follows:

- If a file is being run as a top program file, __name__ is set to the string __main__ when it starts.
- If the file is being imported instead __name__ is set to the modules name as known by its client.

The module can test its own __name__ to determine whether it is being run or imported.

```python
def testing():
    print("Hello from the main file")

if __name__ == "__main__":
    testing()  # only when run and not when imported
```

The most common way we will see the __name__ test applied is for self test code. We can package code that tests a module exports in the module itself by wrapping it in a __name__ test at the bottom of the file. This way can use in client but also test its logic by running it from the shell.

Coding self test code at the bottom of a file under the __name__ test is probably the most common and simplest unit testing protocol in python. It is much more convenient than retyping all our test at the interactive prompt.

## Dual Mode Code
Can use as utilities or run as self test.

## Currency symbols
```python
from formats import money
# use code to specify different country currency.
```

## Help format
```python
import module # module file name
help(module) # full description of the module file
```

## As for import and from
```python
import module as name # use name not module

import module
name = module
del module # dont keep this name

from module import attrname as name
```

## Module Name Clashes: Package and Package Relative Imports
If we have two modules of the same name we may only be able to import one of them by default the one whose directory is leftmost in sys.path list.

We can use either different name of structure our source files in sub directories such that package import directory names make the module references unique. We will be able to access either or both of the same named modules.

This can alos crop up if we accidently use a name for a module of our own that happens to be the same as a standard library module we need.

For this we can either avoid using the same name as another module we need to store our modules in a package directory.  Normal import will skip the package directory (we will get the library version) , but special dotted import statements can still select the local version of the module.

## order matter in top level code
When a module is first imported or reloaded, statement gets executed one by one from the top of the file to the bottom.

- Code at the top level of a module file (not nested in a function) runs as soon as python reaches it during an import because of that it cannot reference names assigned lower in the file.
- Code inside a function body doenpt run until the function is called because names in a function are not resolved until the function actually runs, they can usually reference names anywhere.

## from copies names but doesnt link
The from statement is an assignment to name in the importers scope a name copy not a name aliasing.

```python
# nested1.py
x = 99
def printer(): print(x)

# nested2.py
from nested1 import x, printer
x = 89 # change only here
printer() # output 99
```

If we import two names using from , we get copy of those name not links to them. Changing a name in the importer resets only the binding of the local version of that name, not the name in nested1.py

If we use import to get the whole module and then assign to a qualified however we change the name in nested1.py.

```python
# nested3.py
import nested1
nested1.x = 100
nested1.printer() # 100
```

## The * can obscure the meaning of variables
using import * can overwrite names we are using. It can make it difficult to determing where variable come from and is especially true if the from * form is used on more than one imported file.

```python
from module1 import *
from module2 import *
from module3 import *
# no way to tell what we get

func() # huh duh! what is this function about?
```

The solution is not to do this just try to list the attribute we want in our from the statement. We can avoid if we always use import. 

## reload may not impact from imports