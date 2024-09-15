## Core Types Review and Summary
Some points to remember
- Objects share operations according to their category
- Only mutable objects may be changed in place
- Immutable objects cannot change in place
- Sets are valueless dictionary and are not ordered so sets are neither a mapping nor sequence type.

## Object Classification
| Object Type | Category | Mutable |
|-------------|----------|---------|
| Integer     | Numeric  | No      |
| List        | Sequence | Yes     |
| String      | Sequence | No      |
| Dictionary  | Mapping  | Yes     |
| Set         | Set      | Yes     |
| Files       |  File    | N/A     |
| Tuples      | Sequence | No      |
| Frozenset   | Set      | No      |
| bytearray   | Sequence | Yes     |

## Object Flexibility
- Lists, dictionary and tuple can hold any kind of object
- Sets can contain any type of immutable object
- Lists, dictionary and typle can be arbitrarily nested and can dynamically grow and shrink themself.

## References Versus Copies
- **Assignments always store references to objects not copies of those objects**
- **Changing a mutable object in place may affect other references to the same object elsewhere in our program**
- **slice expressions with empty limits can copy sequence**
- **We can also use copy() or deepcopy()**

## Comparisons, Equality and Truth
Python automatically traverses data structures to apply comparisions from left to right and as deeply as needed. The first difference found along the way determine comparison result.

```python
L1 = [1, ('a', 2)] # same object unique value
L2 = [1, ('a', 2)]
L1 == L2 # will give True (Equivalent or not)
L1 is L2 # will give False (same object or not)
```
`The == operator tests equivalence` and `The is operator test object identity`

```python
String1 = 'spam'
String2 = 'spam'
String1 == String2 # True
String1 is String2 # True because python caches for optimization but when used longer string this will become false.
```

## Comparison
- Numbers are compared by magnitude
- Strings are by lexicographically
- List and Tuple by comparing each component left to right and also for nested structure.
- Sets are equal if both contain the same items
- Dictionaries are equal if sorted (key value) list are equal

## The Meaning of True and False
- Python recognizes and non empty data structure as True and empty data structure as False.
- Numbers are False if zero else True for other value
- None is False

## None object
It is the only value of a special data type in this language which typically serves as an empty placeholder  (like NULL)
None is something not nothing despite its name None.