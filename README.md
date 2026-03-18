# Native Python Bit Array

Native python ```bitarray``` implementation supporting bitwise operations on instances as though the entire array was an integer.

This is similar to but not the same as the PYPI/github package [```bitarray```](https://pypi.org/project/bitarray/).

## **UNDER DEVELOPMENT AND SUBJECT TO CHANGE**

```bitarray```s have some similarities to ```bytearray```s, ```list```s and ```int```s:

- Instantiation:

## Instantiation from ```bytearray``` objects

- Need ```bytearray``` object

```python
from bitarray import bitarray

byte_array = bytearray.fromhex("F0F0")
byte_array
```

- Response showing ```bytearray``` object value.

```python
bytearray(b'\xf0\xf0')
```

- ```bitarray``` from ```bytearray``` object

```python
bit_array = bitarray(byte_array)
bit_array
```

- Response showing ```bitarray``` object value.
  - first from ```__repr__()``` and second from ```__str__()```

```python
<class 'bitarray.bitarray'>: [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1]
>>>
str(bit_array)
'1111000011110000'
```

Note the difference between the two values.  ```__repr__()``` shows the object's internal representation.  Internal representation is done in little-endian style.  That is, the first bit in the list is the least significant bit.  The last bit in the list is the most significant.

```__str__()``` shows the representation as big-endian.  The first bit is the most significant and the last bit is the least significant.  This is more in line with ```bytearray``` representation.

## Instantiation from ```int``` or integer values

```python
from bitarray import bitarray

# hex representation
bitarray(0xFF)
# integer representation
bitarray(255)
```

Responses to the above would both look the same since ```0xFF``` equals ```255```.

```python
>>> from bitarray import bitarray
>>> bitarray(255)
bitarray: [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>>
>>> bitarray(0xFF)
bitarray: [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
>>>
```

**```bitarray``` objects do not support negative values.**  Think of them as being extremely large unsigned integers.  In Python 3.0 and above, any integer can be as large as desired up to the underlying hardware and operating system limits.

```python
from bitarray import bitarray

len(bitarray(2**(2**1000)))
```

These results to the above were achieved on a computer with 64 GB RAM.  The last seen memory usage by the Python process showed it had allocated over 52 BG RAM.  The program ran at most another hour before crashing.

```python
>>> from bitarray import bitarray
>>> len(bitarray(2**(2**1000)))
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    len(bitarray(2**(2**1000)))
                 ~^^~~~~~~~~~
MemoryError
>>> 2**1000
10715086071862673209484250490600018105614048117055336074437503883703510511249361224931983788156958581275946729175531468251871452856923140435984577574698574803934567774824230985421074605062371141877954182153046474983581941267398767559165543946077062914571196477686542167660429831652624386837205668069376
>>>>>> len(bitarray(2**1000))
1008
>>> len(bitarray(2**1000))/8
126.0
>>>
```

After the MemoryError, just to see how big ```2**1000``` is, the result of those calculations are shown above.  There were 1,008 bits and 126 bytes.  That would be a very big integer on its own.  Note that the number of bits in a ```bitarray``` object instantiation may include padding bits to bring them to byte boundaries.  That is, an object that is created by 6 bits will be extended to 8 bits so that the instantiation finishes on a byte boundary.

## Instantiation from ```bitarray``` objects

The best way to copy a ```bitarray``` object is to use it to create a new ```bitarray``` object as shown below.  This allows the new ```bitarray``` to be changed without changing the original object.

```python
from bitarray import bitarray

original_bitarray = bitarray(0xFF)
copy_bitarray = bitarray(original_bitarray)
original_bitarray == copy_bitarray
```

## Converting ```bitarray``` objects to integers

```python
from bitarray import bitarray

bitarray_object = bitarray(255)

integer_value = bitarray_object.to_int()
```

## Converting ```bitarray``` objects to ```bytearray```

```python
from bitarray import bitarray

bitarray_object = bitarray(bytearray.fromhex("FFEEDDCCBBAA99887766554433221100"))

bytearray_value = bitarray_object.to_bytearray()

print(bytearray_value.hex())

integer_value = bitarray_object.to_int()

print(f"{integer_value:x}")
```

## Comparison operators and ```bitarray``` objects

```bitarray``` objects can be compared to ```bytearray``` objects, integers and ```bitarray``` objects.

```python
form bitarray import bitarray

bitarray_value = 255

low_bitarray_value   = bitarray(10)
equal_bitarray_value = bitarray(bytearray.fromhex("FF"))
high_bitarray_value  = bitarray(bytearray.fromhex("FFFFFFFFFFFFFFFFFFFFFF"))

print(f"low_bitarray_value > bitarray_value: {low_bitarray_value > bitarray_value}")
print(f"low_bitarray_value < bitarray_value: {low_bitarray_value > bitarray_value}")
print(f"low_bitarray_value >= bitarray_value: {low_bitarray_value >= bitarray_value}")
print(f"low_bitarray_value <= bitarray_value: {low_bitarray_value >= bitarray_value}")
print(f"low_bitarray_value != bitarray_value: {low_bitarray_value != bitarray_value}")
print(f"low_bitarray_value == bitarray_value: {low_bitarray_value == bitarray_value}")

print(f"equal_bitarray_value > bitarray_value: {equal_bitarray_value > bitarray_value}")
print(f"equal_bitarray_value < bitarray_value: {equal_bitarray_value < bitarray_value}")
print(f"equal_bitarray_value >= bitarray_value: {equal_bitarray_value >= bitarray_value}")
print(f"equal_bitarray_value <= bitarray_value: {equal_bitarray_value <= bitarray_value}")
print(f"equal_bitarray_value != bitarray_value: {equal_bitarray_value != bitarray_value}")
print(f"equal_bitarray_value == bitarray_value: {equal_bitarray_value == bitarray_value}")

print(f"high_bitarray_value > bitarray_value: {high_bitarray_value > bitarray_value}")
print(f"high_bitarray_value < bitarray_value: {high_bitarray_value < bitarray_value}")
print(f"high_bitarray_value >= bitarray_value: {high_bitarray_value >= bitarray_value}")
print(f"high_bitarray_value <= bitarray_value: {high_bitarray_value <= bitarray_value}")
print(f"high_bitarray_value != bitarray_value: {high_bitarray_value != bitarray_value}")
print(f"high_bitarray_value == bitarray_value: {high_bitarray_value == bitarray_value}")
```

## Using ```bitarray``` as a list

Many of the capabilities made available by lists are also available through ```bitarray```.

Some examples are shown below:

```python
from bitarray import bitarray

print(f"0 in bitarray(0xFFFFFFFF): {0 in bitarray(0xFFFFFFFF)}")
print(f"1 in bitarray(0xFFFFFFFF): {1 in bitarray(0xFFFFFFFF)}")

print(f"len(bitarray(0xFF))): {len(bitarray(0xFF))}")
print(f"len(bitarray(0xFFFFFFFF)): {len(bitarray(0xFFFFFFFF))}")

print(f"len(bitarray(0xFF, max_int_bits=8)): len(bitarray(0xFF, max_int_bits=8))")
print(f"len(bitarray(0xFF, max_int_bits=16)): len(bitarray(0xFF, max_int_bits=16))")

# in-place operations
#   - __setitem__(self, key, value) - in-place changing value
value = bitarray(0xFF, max_int_bits=8)
value[0] = 0
value[1] = 0
value[2] = 0
value[3] = 0
print(f"value: 0x{value.to_int():x}")

#   - __delitem__(self, key) - in-place deleting
value = bitarray(0xFF, max_int_bits=8)
print(f"del value[0:4]: {value}")
del value[0:4]

value = bitarray(0xFF, max_int_bits=8)
del value[-4]
print(f"del value[-4]: {value}")

#   - extend(iterable) - in-place extending
value = bitarray(0XFF, max_int_bits=8)
value.extend(bitarray(0x11, max_int_bits=8))

#   - clear() - in-place clearing
#   NOTE: len(value.clear()) raises TypeError: object of type 'NoneType' has no len()
value = bitarray(0XFF)
len(value)
value.clear()
len(value)

#   - insert(index, element) - in place insert
value = bitarray(0xFF, max_int_bits=8)
len(value)
value.insert(0, bitarray(0xFF, max_int_bits=8))
len(value)

#   - append(element) - in-place append
value = bitarray(0, max_int_bits=8)
len(value)
value.to_int()
value.append(bitarray(0xFF, max_int_bits=8))
len(value)
value.to_int()

#   - reverse() - in-place reversal of elements
value = bitarray(0x0123456789ABCDEF)
value.to_bytearray().hex()
value.reverse()
value.to_bytearray().hex()

#   - reversed() - returns a reversed bitarray
value = bitarray(0x0123456789ABCDEF)
reverse_value = value.reversed()
value.to_bytearray().hex()
reverse_value.to_bytearray().hex()
reverse_reverse_value = reverse_value.reversed()
reverse_reverse_value.to_bytearray().hex()
```

## Using bitwise and logical operators on ```bitarray```

```python
from bitarray import bitarray

# <<	__lshift__(self, rhs:int)	Left Shift
bitarray(0x0F, max_int_bits=8) << 4

# >>	__rshift__(self, rhs:int)	Right Shift
bitarray(0xF0, max_int_bits=8) >> 4

#  & and (__and__/__rand__) 
bitarray(0xF1, max_int_bits=8) & bitarray(0x01, max_int_bits=8)

#  | or  (__or__/__ror__)
bitarray(0xF1, max_int_bits=8) | bitarray(0x01, max_int_bits=8)

#  ^ xor (__xor__/__rxor__)
bitarray(0xF1, max_int_bits=8) ^ bitarray(0x01, max_int_bits=8)

#  ~ not (__invert__)
~bitarray(0xF0, max_int_bits=8)
```

## Python Project Software Build and Installation

For this project, [```uv```](https://github.com/astral-sh/uv) is used to

- Install Python
- Create and manage the virtual Python runtime environment
- Create a Python package and install it into the virtual environment
- Run specific Python modules installed in the virtual environment

Install ```git``` before cloning the software from this [github repository](https://github.com/thatlarrypearson/bitarray).  For a Windows or Mac ```git``` installation, go to [Microsoft Learn - Install and set up Git](https://learn.microsoft.com/en-us/devops/develop/git/install-and-set-up-git) and follow their instructions.

Use the ```apt``` package management system to install ```git``` on Debian Linux variants including Raspberry Pi, Ubuntu and Linux Mint.

```bash
apt install git
```

For Windows (and Mac) users, [GitHub Desktop](https://desktop.github.com/download/) is a GUI interface simplifying development workflows.

To install [```uv```](https://github.com/astral-sh/uv), follow these [```uv``` install instructions](https://docs.astral.sh/uv/getting-started/installation/)

After installing and testing [```uv```](https://github.com/astral-sh/uv), use [```git```](https://git-scm.com/downloads) to [clone this repository](https://github.com/thatlarrypearson/bitarray) onto your local target computer.

```bash
# Clone the git repository
git clone https://github.com/thatlarrypearson/bitarray.git
```

Next, use [```uv```](https://github.com/astral-sh/uv) to prepare the virtual Python environment, install the needed Python version (if needed), install the required external Python libraries, build [Vehicle Telemetry System software](https://github.com/thatlarrypearson/bitarray), install [```bitarray```](https://github.com/thatlarrypearson/bitarray) and run a simple test of the newly installed software.

```bash
# get into the cloned repository directory
cd bitarray

# create the virtual Python environment with the needed libraries
# by using the ```dependencies``` in the ```pyproject.toml``` file
uv sync

# Activate the Python Virtual Environment

# Windows PowerShell
.\.venv\Scripts\activate

# Linux/Mac bash Shell
source .venv/bin/activate

# When the Python Virtual Environment is activated, the prompt will change.

# Windows PowerShell
#     - (bitarray) PS C:\Users\username\bitarray >

# Linux/Mac bash Shell
#     - (bitarray) user@hostname:~/bitarray $

uv build .

# Developers and data analysts install the software such that changes are reflected
# in the virtual runtime environment automatically.
uv pip install -e .

# For production use, install the software as a Python package.
uv pip install dist/bitarray-0.0.0-py3-none-any.whl
```

## Simple Tests Validating Build and Installation

Before running any module, be sure to activate the Python virtual environment.

```bash
# get into the cloned repository directory
cd bitarray

# Activate the Python Virtual Environment

# Windows PowerShell
.\.venv\Scripts\activate

# Linux/Mac bash Shell
source .venv/Scripts/activate
```

Once the Python virtual environment is activated, run the tests as shown below.  Resolve any errors before continuing.

```bash
# Windows PowerShell
python -m pytest -v .\tests

# Linux/Mac bash Shell
python -m pytest -v ./tests
```

Results should look something like the following:

```powershell
(bitarray) PS bitarray> python -m pytest -vv .\tests
================================== test session starts ===================================
platform win32 -- Python 3.13.3, pytest-9.0.2, pluggy-1.6.0 -- bitarray\.venv\Scripts\python.exe
cachedir: .pytest_cache
rootdir: bitarray
configfile: pyproject.toml
collected 10 items

tests/test_01_methods_to_from_int.py::test_instantiation_int
PASSED                                                                              [ 10%]
tests/test_02_methods_to_from_bytearray.py::test_instantiation_bytearray
PASSED                                                                              [ 20%]
tests/test_03_methods_to_from_list.py::test_instantiation_bytearray
PASSED                                                                              [ 30%]
tests/test_04_slicing.py::test_slicing
PASSED                                                                              [ 40%]
tests/test_05_add_eq.py::test_add_eq
PASSED                                                                              [ 50%]
tests/test_06_comparison.py::test_comparison
PASSED                                                                              [ 60%]
tests/test_07_shifting.py::test_shifting
PASSED                                                                              [ 70%]
tests/test_08_logical_operators.py::test_logical_operators
PASSED                                                                              [ 80%]
tests/test_09_arithmetic_operators.py::test_arithmetic_operators
PASSED                                                                              [ 90%]
tests/test_10_list_operations.py::test_list_operations
PASSED                                                                              [100%]

============================== 10 passed in 0.06s ================================++++====
(bitarray) PS bitarray>
```

## License

Copyright 2026 Larry Pearson all rights reserved.  This software is available under the [MIT License](License.md).
