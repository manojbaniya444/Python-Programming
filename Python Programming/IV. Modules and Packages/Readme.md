## Modules and Packages

Module - the highest level program organization unit which packages program code and data for reuse and provides self contained namespaces that minimize variable name clashes across our programs.

Each file is a module and modules import other modules to use thte names they define.

`import` lets a client (importer) fetch a module as a whole
`from` allows clients to fetch particular names from a module
`imp.reload` provide a way to reload a modules code without stopping python

## Why use Modules

They provide an easy way to organize components into a system by serving as self contained packages of variables known as namespaces.

- code reuse
- system namespace partitioning
- implementing shared services or data

## How to structure program

At base level python program consist of text files containing statement with one main top level file and zero or more supplemental files known as modules.

The top level (script) contain the main flow of control of our program and this file is run as main file. The modules files are libraries of tools used to collect components used by the top level file and possibly elsewhere.

As the import is executing object defined by a module are also created at runtime.

Along the way, every name assigned at the top level of the file becomes an attribute of the module, accessible to importers.

## Standard library modules:

Python automatically comes with a large collection of utility modules known as the standard libray. This collection over 200 modules large at last count contains platform independent support for commong programming task:`OS interfaces`,`network and internet scripting`. `GUI construction` and much more.

## How imports work:

Three step process but only one time:

- Find the modules file
- Compile it ( if necessary )
  Compile if the byte code file is older than the source file and dont compile if .pyc byte code file is not that older than the corresponding source file that was created by the same python version, it skips the source to byte code compile step.
- Run it
  Executes byte code of module.

## Byte code files: '__pycache__'

To speed startups, it will try to save byte code in a file in order to skip the compile step next time around. Byte code is instead stored in files in a subdirectory named `__pycache__.`

## The Module search path:
First step of module is locating the file to be imported because we may need to tell python where to look to find files to import we need to know how to tap into its search path in order to extend it.

I. HOME DIRECTORY (Automatic)
Python first looks for the imported file in the `**home directory**`. If a program is located entirely in a single directory all of its imports will work automatically with no configuration of path required. But its files will also `override` modules of the same name in directory.

II. PYTHONPATH DIRECTORIES (Configurable)
Next python searches all directories listed in our `**PYTHONPATH**` environment variable setting. It is a simple a list of user defined and platform specific names of directories that contain python code files.

III. STANDARD LIBRARY DIRECTORIES (Automatic)
Python automatically search the directories where the standard library modules are installed on our machines and no need to be added to PYTHONPATH.

IV. .PATH FILE DIRECTORY (configurable)
List the directories to the modules search path by simply listing them one per line in a text file whose name ends with `.pth` suffix.

## The from statement
Allows us to use the copied names directly in the script without going through the module
```python
from module import method
method()
```

## The from * statement
We use `*` instead of specific names, we get copies of all the names (no need to specify) assigned at the top level of the referenced module.
```python
from module import * # copies out all variables
function()
```

## Import happen only once
Often report that the first import works fine but later imports during an interactive session (run) seem to have no effect.

Modules are loaded and run on the first import or from and only the first. This is on purpose because importing is an expensive operation by default python does it just once per file per process.Later import operations simply fetch the already loaded module object.

## import and from are Assignments
Just like def,  import and from are executable statements not compile time declarations, imported modules and names are not available until their associated import or run statements run.

```python
# cross file name changes
from small import x, y # copy two names out
x = 1 # change x here only

import small # get module name
small.x = 9 # changes x in other module
```

## When import is required
Import instead of from when we use the same name defined in two different module.
```python
from M import func
from N import func
func() # calls N.func() only

import M, N
N.func()
M.func()
```

## Consider the notion of module loading and scope
- Module statements run on the first import: (from top to bottom when imported first time anywhere in system)
- Top level assignments create module attributes
```python
module.py
X = 9 # top level assignment

import module
module.x # from module (act as global variable for all who import it.)
```
- Module namespaces can be accessed via the attribute `**__dict__**` or `dir(M)`
- Modules are a single scope

```python
# during this import python will run all the code from module_a
import module_a
# then will run module_b code
import module_b

# Then the statement own script
print("Top level module")

# View the __dict__
print(list(module_a.__dict__.keys()))
print([attr for attr in module_a.__dict__ if not attr.startswith("__")])

# Then attributes and objects of modules can run
module_a.attr
module_b.func

# The statement at the end of the main script
print("Top level statement")
```

## Import and scope
```python
module.py

x = 9
def f():
    global x
    x = 1

X = 11
import module
module.f()
print(X, module.X) # This will print 11, 1 because global is only for the module file, global in module doesnt affect the variable of importing module.
```
In other words import operations never give upward visibility to code in imported files.
- Function can never see name in other function unless they are physically enclosing.
- Module code can never see names in other modules unless they are imported explicitely.

## Reloading Modules
Modules code is run only once per process by default. To force a module code to be reloaded and rerun we need to call the `**reload**` build in function.

The reload function allows parts of a program to be changed withour stopping the whole program.

Reloading offers further advantage in performance.

- reload runs a module files new code in the modules current namespace
- Top level assignments in the file replace names with new values
- reloads impact all clients that use import to fetch modules
- reloads impaact future from clients only (module imported by from in the past wont be affected by a reload)
- reloads apply to a single module only

## Module Packages
[Module Packages Import Here](./Module%20Packages%20Import/)