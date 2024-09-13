# How Python Runs Programs
## Python Interpreter
An `Interpreter` is a kind of program that executes other programs. When we write a Python program, the python interpreter reads our program and carries out the instructions it contains.
In effect, the interpreter is a layer of software logic between our code and the computer hardware on our machine.

When the Python package is installed on our machine, it generates a number of components: `Interpreter` and a `Support Library`. Depending on how we use it, the Python interpreter may take the form of an executable program, or a set of libraries linked into another program. Whatever form it takes, the Python code we write must always be run by this interpreter and to enable that, we must install a Python interpreter on our computer.

## Program Execution: Programmers View
In the simplest form , a Python program is just a text file containing Python statements. Python program files are given names that end in `.py`.
After this we must tell Python to `execute` the file which simply means to run all the statements in the file from top to bottom and one after another.

## Program Execution: Python view
We type code into text files, and we run those files through the interpreter. Under the hood, though, a bit more happens when we tell Python to go.
Specifically the python code is first compiled to something called `byte code` and then routed to something called `virtual machine`.

### Byte code compilation
Internally and almost completely hidden, when we execute a program Python first compiles our **source code**  into a format known as **byte code**.

> Byte code is a lower level platform independent representation of our source code.
If the Python process has write access on our machine, it will store the byte code of the programs in files that end with a `**pyc**` extension **.py source**.
We will see these files show up on our computer after we have run a few programs alongside the corresponding source code files that is in the same directories.

For instance, we will notice a **script.pyc** after importing **script.py**.
In 3.2 ver and later, Python instead saves its .pyc byte code files in a subdirectory named `__pycache__` located in the directory where our source files reside and in files whose names identify the Python version that created them.

The **__pycache__* subdirectory helps to avoid clutter, and the new naming convention for byte code files prevents different python versions installed on the same computer from overwriting each other's saved byte code.

Python saves byte code like this as a startup speed optimization. The next time we run our program, it will load the .pyc files and skip the compilation step as long as we have not changed the source code since the byte code was last saved and are not running a different Python than the one that create the byte code.

What trigger a new byte code file:
- Change in source code
- Python version differing

Byte code files are also one way to ship Python programs.

> Byte code files are saved for only files that are imported for the files of a program that are only run as scripts.

### The Python Virtual Machine (PVM)
Once our program has been compiled to byte code, it is shipped off for execution to something generally known as the **Python Virtual Machine`PVM`**.

PVM is not a separate program and it need not be installed by itself. The `PVM` is just a big code loop that iterates through our byte code instructions onebyone to carry out instructions. The PVM is the `runtime` engine of Python. Technically it is just the last step of what is called the **Python Interpreter**.

> Python byte code is not binary machine code. Byte code is a Python's specific representation. This is why some code may not run as fast as C or C++.

> There is really no distinction between the development and execution environments. The systems that compile and execute our source code are really one and same.

## Implementation of Python Alternatives
- CPython: The standard
- Jython: Python for Java
- IronPython: Python for .NET
- Stackless: Python for concurrency
- PyPy: Python for speed

## Execution Optimization Tools
Optimize the basic execution model.
- Cython: A Python/C hybrid
- Shed Skin:Python 2 C++ translator
- Psyco: The original Just in Time compiler

## Frozen Binaries
When asking a real python compiler, a way to generate standalone binary executables from the Python programs: `**Frozen Binaries**`. These programs can be run without requiring a Python installation.

Frozen binaries bundle together the byte code of our program files along with the `PVM` and any python support files that our program needs into a single package. Byte code and PVM are merged into a single component: a frozen binary file.