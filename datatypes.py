# Data Types

"""

Text Type : str

Numberic Types : int, float, complex

Sequence Types : list, tuple, range

Mapping Type : dict

Set Types : set, frozenset

Booleann Type : bool

Binary Types : bytes, bytearray, memoryview

None Type : NoneType

"""

# getting the data type by using type()

x = 5
print(type(x))

# setting the data type

# Text Type

x = "str"
print(type(x)) #string type

# Numeric Types

x = 1
print(type(x)) #int type

x = 1.0
print(type(x)) #float type

x = 1j
print(type(x)) #complex type

# Sequence Types

x = [1,2,3]
print(type(x)) #list type

x = (1,2,3)
print(type(x)) #tuple type

x = range(6)
print(type(x)) #range type

# Dict Type

x = {"name":1,"age":2}
print(type(x)) #dict type

# Set types

x = {1,2,3}
print(type(x)) #set type

x = frozenset({1,2,3})
print(type(x)) #fronzen type

# Boolean type

x = True
print(type(x)) #boolean type

# Byte Types

x = b"Hello"
print(type(x)) #bytes type

x = bytearray(5)
print(type(x)) #byte array type

x = memoryview(bytes(5))
print(type(x))

# None Type

x = None
print(type(x)) #none type




