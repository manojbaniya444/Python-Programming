## Module Package

In addition to a module name an import can name a directory path. A directory of python code is said to be a `**PACKAGE**`, so such imports are known as package imports.

This is advanced feature but the hierarchy it provides turns out to be handy for organizing the files in a large system and tends to simplify module search path setting.

## Package Import: Basic concept

In the place where we have been namin a simple file in our `import` statements, we can instead list a path of names separated by periods.

```python
# both dir1 and dir2 must contain __init__.py file
# dir() must be listed on the module search path sys.path
import dir1.dir2.module # can give name not defined NameError

from dir1.dir2.module import x
```

> We cannot use any platform specific path syntax in our import statement only use period separated.

## Package `__init__.py` File:

Each directory named within the path of a package import statement must contain a file named `__init__.py`, or our package imports will fail. That is in the above package import both **dir1** and **dir2** must contain a file named `**__init__.py**`. The container dir() does not require such file because it is not listed in the import statement itself but it must be listed on the module search path `**sys.path**`.

The `__init__` file can contain python code as other and their names are special because their code is run automatically the first time a python program imports a directory, and thus serves primarily as a hook for performing initialization steps required by the package. These files can also be completely empty though and sometimes have additional roles.

> Use import instead of from with packages only if we need to access the same attribute name in more than 2 paths. The as extension in from can also be used to provide unique synonyms

```python
import system1.utilities
import system2.utilities
system1.utilities.function("hello")
system2.utilities.function("hey")
```

## Relative Import
`from` statement use leading dots(".") to specify that they require modules located within the same package instead of modules located elsewhere on the module import search path.
```python
# only search in the current directory and will not look for same name module located elsewhere.
from . import spam # relative to this package

# relative then absolute
# from a module named spam located in the same package import the variable spam
from .spam import spam
```

```python
# other dot based reference are also possible
from .string import name1, name2 # Imports names from dir.string
from . import string
from .. import string # Imports string sibling of mypkg
```
## The scope of relative imports
- Relative import apply to import within package only
- Relative import apply to the from statement only

```python
# \mypkg
#       __init__.py
#       main.py
#       String.py

# /main.py
import String # Imports string outside package (absolute) so we will get python String object

from . import String # Import mypkg.String here (relative)

from String import name # Imports name from string outside package

from .String import name # Imports mypkg.String name attribute

from mypkg import String # Imports mypkg.String here because a file can sometimes name its own package explicitly in an absolute import statement relative to a directory on sys.path
```
> If we add a module of the same name in the directory we are working in it is selected because the first entry on the module search path is the current working directory.