# bitarray/src/bitarray.py

from typing import Self
from itertools import batched
from math import ceil
from sys import stderr

DEFAULT_MAX_INT_BITS = 32
DEFAULT_BYTE_SIZE = 8

class bitarray():
    # 'data' is an array of integers where the items in the array
    # are constrained to be either 0 or 1.
    # These are arranged so that the most significant bits (bigger values)
    # are indexed with higher positional values than less significant bits.
    # When converting to/from 'bytearray` type values using bitarray.to_bytearray/bitarray.from_bytearray,
    # this implementation assumes network byte order (e.g. network order) is being used.
    # See https://en.wikipedia.org/wiki/Endianness#Networking for a description of network order.
    # See https://rszalski.github.io/magicmethods/#comparisons for a description of magic methods
    data = None

    def __init__(
            self,
            bits:(Self | list | int | bytearray | str),
            max_int_bits:int=DEFAULT_MAX_INT_BITS
        ):
        if isinstance(bits, list):
            self.init_from_list(bits)

        elif isinstance(bits, int):
            self.init_from_int(bits, int_size=max_int_bits)

        elif isinstance(bits, bytearray):
            self.init_from_bytearray(bits)

        elif isinstance(bits, type(self)):
            self.data = list(bits.data)

        elif bits is not None:
            raise ValueError(f"Invalid Value Type ({type(bits)}) for bits")

        self.data == []

    # +	__add__(self, other)	Addition
    def __add__(self, rhs:(Self | bytearray | int)) -> (Self | bytearray | int):
        if not isinstance(rhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't add with {type(rhs)}")
        if isinstance(rhs, int):
            return_value = self.to_int() + rhs
            if return_value >= 0:
                return ((type(self))(return_value))
            raise ValueError("Arithmetic operation would yield forbidden negative value.")
        return (type(self))(self.to_int() + (type(self))(rhs).to_int())

    def __radd__(self, lhs:(Self | bytearray | int)) -> (Self | bytearray | int):
        if not isinstance(lhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't add with {type(lhs)}")
        if isinstance(lhs, int):
            return_value = lhs + self.to_int()
            if return_value >= 0:
                return ((type(self))(return_value))
            raise ValueError("Arithmetic operation would yield forbidden negative value.")
        return ((type(self))((type(self)(lhs).to_int()) + self.to_int()))


    # -	__sub__(self, other)	Subtraction
    def __sub__(self, rhs:(Self | bytearray | int)) -> Self:
        if not isinstance(rhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't subtract with {type(rhs)}")

        if self.to_int() >= (type(self))(rhs).to_int():
            return (type(self))(self.to_int() - (type(self))(rhs).to_int())

        raise ValueError(
            "right-hand side greater than left-hand side causing unsupported negative bitarray value"
        )

    def __rsub__(self, lhs:(Self | bytearray | int)) -> Self:
        if not isinstance(lhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't subtract with {type(lhs)}")

        if (type(self))(lhs).to_int() >= self.to_int():
            return ((type(self))((type(self)(lhs).to_int()) - self.to_int()))

        raise ValueError(
            "left-hand side greater than right-hand side causing unsupported negative bitarray value"
        )

    # - __neg__(self) - unary operator
    def __neg__(self):
        raise NotImplementedError("bitarray is assumed to be unsigned. Negative values not allowed.")

    # *	__mul__(self, other)	Multiplication
    def __mul__(self, rhs:(Self | bytearray | int)) -> Self:
        if not isinstance(rhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't multiply with {type(rhs)}")
        if isinstance(rhs, int) and rhs < 0:
            raise ValueError(
                "negative right-hand side causing unsupported negative bitarray value"
            )

        return (type(self))(self.to_int() * (type(self))(rhs).to_int())

    def __rmul__(self, lhs:(Self | bytearray | int)) -> Self:
        if not isinstance(lhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't multiply with {type(lhs)}")

        if isinstance(lhs, int) and lhs < 0:
            raise ValueError(
                "negative left-hand side causing unsupported negative bitarray value"
            )

        return ((type(self))((type(self)(lhs).to_int()) * self.to_int()))

    # /	__truediv__(self, other)	Division
    # truediv (/): This is the standard division operator (/).
    # It always performs floating-point division, meaning the
    # result will be a float, even if both operands are integers
    # and the result is a whole number.
    def __truediv__(self, rhs:(Self | bytearray | int)) -> float:
        if not isinstance(rhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't divide with {type(rhs)}")

        return (self.to_int() / (type(self))(rhs).to_int())

    def __rtruediv__(self, lhs:(Self | bytearray | int)) -> float:
        if not isinstance(lhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't divide with {type(lhs)}")

        return ((type(self)(lhs).to_int()) / self.to_int())

    # // __floordiv__(self, other)
    # Rounding Behavior: The method should return the largest integer less than or equal
    # to the mathematical quotient, consistent with Python's standard //
    # operator which rounds towards negative infinity.
    def __floordiv__(self, rhs:(Self | bytearray | int)) -> Self:
        if not isinstance(rhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't divide with {type(rhs)}")

        if isinstance(rhs, int) and rhs < 0:
            raise ValueError(
                "negative right-hand side causing unsupported negative bitarray value"
            )

        return (type(self))(self.to_int() // (type(self))(rhs).to_int())

    def __rfloordiv__(self, lhs:(Self | bytearray | int)) -> Self:
        if not isinstance(lhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't divide with {type(lhs)}")

        if isinstance(lhs, int) and lhs < 0:
            raise ValueError(
                "negative left-hand side causing unsupported negative bitarray value"
            )

        return ((type(self))((type(self)(lhs).to_int()) // self.to_int()))

    # % __mod__(self, other)
    # returns the remainder when an integer divides an integer
    def __mod__(self, rhs) -> Self:
        if not isinstance(rhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't divide with {type(rhs)}")

        return (type(self))(self.to_int() % (type(self))(rhs).to_int())

    def __rmod__(self, lhs) -> Self:
        if not isinstance(lhs, (type(self), bytearray, int)):
            raise NotImplementedError(f"bitarray doesn't divide with {type(lhs)}")

        return ((type(self))((type(self)(lhs).to_int()) % self.to_int()))

    # ** __pow__(self, other) 
    def __pow__(self, rhs:(Self | bytearray | int))->Self:
        if isinstance(rhs, (bytearray, int)):
            rhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        if isinstance(rhs, int) and rhs < 0:
            raise ValueError("Negative power (**) operator cannot be used with bitarray().")

        return (type(self))(self.to_int() ** (rhs).to_int())

    def __rpow__(self, lhs:(Self | bytearray | int))->Self:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        if isinstance(lhs, int) and lhs < 0:
            raise ValueError("Negative operand cannot be used with bitarray() operator (**).")

        return (type(self))(self.to_int() ** (lhs).to_int())

    # ==	__eq__(self, other)	Equality
    def __eq__(self, rhs:(Self | bytearray | int)) -> bool:
        if isinstance(rhs, (bytearray, int)):
            rhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return self.to_int() == rhs.to_int()

    def __req__(self, lhs:(Self | bytearray | int)) -> bool:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return lhs.to_int() == self.to_int()

    # <	__lt__(self, other)	Less than
    def __lt__(self, rhs:(Self | bytearray | int)) -> bool:
        if isinstance(rhs, (bytearray, int)):
            rhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return self.to_int() < rhs.to_int()

    # __rlt__(self, other) Less than
    def __rlt__(self, lhs:(Self | bytearray | int)) -> bool:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return lhs.to_int() < self.to_int()

    # __gt__(self, other) Greater than
    def __gt__(self, lhs:(Self | bytearray |int))->bool:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return lhs.to_int() < self.to_int()

    # __rgt__(self, other) Greater than
    def __rgt__(self, rhs:(Self | bytearray | int))->bool:
        if isinstance(rhs):
            rhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return self.to_int() < rhs.to_int()

    # __le__(self, other): Less than or equal to
    def __le__(self, rhs:(Self | bytearray | int)) -> bool:
        if isinstance(rhs, (bytearray, int)):
            rhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return self.to_int() <= rhs.to_int()


    # __rle__(self, other): Less than or equal to
    def __rlt__(self, lhs:(Self | bytearray | int)) -> bool:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return self.to_int() <= lhs.to_int()

    # __ge__(self, other): Greater than or equal to
    def __ge__(self, rhs:(Self | bytearray | int)) -> bool:
        if isinstance(rhs, (bytearray, int)):
            rhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return rhs.to_int() <= self.to_int()

    # __rge__(self, other): Greater than or equal to
    def __rle__(self, lhs:(Self | bytearray | int)) -> bool:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return self.to_int() <= lhs.to_int()

    # __ne__(self, other): not equal to
    def __ne__(self, rhs:(Self | bytearray | int)) -> bool:
        if isinstance(rhs, (bytearray, int)):
            rhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return rhs.to_int() != self.to_int()

    # __rne__(self, other): not equal to
    def __rne__(self, lhs:(Self | bytearray | int)) -> bool:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return self.to_int() != lhs.to_int()

    # &	__and__(self, other)	    Bitwise AND
    def __and__(self, rhs:(Self | bytearray | int)) -> Self:
        if isinstance(rhs, (bytearray, int)):
            rhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return (type(self))(self.to_int() & rhs.to_int())

    def __rand__(self, lhs:(Self | bytearray | int)) -> Self:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return (type(self))(lhs.to_int() & self.to_int())

    # |	__or__(self, other)	        Bitwise OR
    def __or__(self, rhs:(Self | bytearray | int)) -> Self:
        if isinstance(rhs, (bytearray, int)):
            rhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return (type(self))(self.to_int() | rhs.to_int())

    def __ror__(self, lhs:(Self | bytearray | int)) -> Self:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        return (type(self))(lhs.to_int() | self.to_int())


    # ^	__xor__(self, other)	    Bitwise XOR
    def __xor__(self, rhs:(Self | bytearray | int)) -> Self:
        if isinstance(rhs, (type(self), bytearray, int)):
            rhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return (type(self))(self.to_int() ^ rhs.to_int())

    def __rxor__(self, lhs:(Self | bytearray | int)) -> Self:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        return (type(self))(lhs.to_int() ^ self.to_int())

    # ~	__invert__(self)	        Bitwise NOT (Unary)
    # Because bitarray assumes all integers are unsigned integers regardless of size,
    # this doesn't work like the Python integers.  That is, the result does not work
    # like ~ operator in Python which is defined mathematically as -(x+1).
    # In this implementation, literally, each bit is flipped to its opposite.
    def __invert__(self) -> Self:
        return (type(self))([0 if i == 1 else 1 for i in self.data], max_int_bits=len(self.data))

    # <<	__lshift__(self, other)	Left Shift
    def __lshift__(self, rhs:int) -> Self:
        if not isinstance(rhs, int):
            raise TypeError("argument 'rhs' must be of type 'int'")

        return (type(self))(self.to_int() << rhs)

    # >>	__rshift__(self, other)	Right Shift
    def __rshift__(self, rhs:int) -> Self:
        return (type(self))(self.to_int() >> rhs)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index:(int | slice)) -> Self:
        if not isinstance(index, (slice, int)):
            raise ValueError(f"Invalid Index of type {type(index)}")

        return_value = self.data[index]

        if isinstance(return_value, int):
            return (type(self))(return_value, max_int_bits=len(self.data))
        
        return (type(self))(return_value)

    def __setitem__(self, index:(int | slice), value:(int | list)):
        if isinstance(index, slice) and isinstance(value, list) and hasattr(value, "__iter__"):
            self.data[index] = value
            return
        elif isinstance(index, int) and isinstance(value, int):
            self.data[index] = value
            return

        raise TypeError(f"Invalid Value Type ({type(value)}) for 'value' when slicing or indexing")

    def __delitem__(self, index:(int | slice)):
        if isinstance(index, (slice, int)):
            del self.data[index]
            return

        raise TypeError(f"Invalid Value Type ({type(value)}) for 'value' when slicing or indexing")

    def __repr__(self)->str:
        # representation appears as little endian
        return f"{type(self)}: {self.data}"

    def __str__(self)->str:
        # returns big endian string to match network byte order
        # don't use this for instantiation
        return "".join(([f"{i}" for i in self.data]).reverse())

    def insert(self, index:int, value:int):
        if not isinstance(value, int):
            raise TypeError(f"value type ({type(value)}) not an int")

        if value in {0, 1}:
            self.data.insert(index, value)
        else:
            raise ValueError(f"value ({value}) not 0 or 1")

    def append(self, value:(int | list | bytearray)):
        if isinstance(value, int) and value in {0, 1}:
            self.data.append(value)
            return
        
        if isinstance(value, int):
            raise ValueError(f"append value ({value}) not 0 or 1")

        if isinstance(value, bytearray):
            value = bitarray(value).data
        
        if isinstance(value, type(self)):
            value = value.data

        if isinstance(value, list):
            for item in value:
                if isinstance(item, int) and item in {0, 1}:
                    self.data.append(item)
                else:
                    raise ValueError(f"list item ({item}) not 0 or 1 integer value")
            return

        raise TypeError(f"type {type(value)} not an int or list with values 0 or 1")

    def extend(self, value:list):
        self.data.extend(value)

    def clear(self):
        del self.data[:]

    def reverse(self):
        # reverses the original list
        self.data.reverse()

    def reversed(self):
        # reverses a copy
        return (type(self))(list(self.data[::-1]))

    def init_from_list(self, bit_list: list):
        # ensure list fits byte boundaries
        ideal_list_size = ceil(len(bit_list)/DEFAULT_BYTE_SIZE) * DEFAULT_BYTE_SIZE
        self.data = [0 for _ in range(ideal_list_size)]

        for i, bit in enumerate(bit_list):
            if not isinstance(bit, int) or bit not in [0, 1]:
                raise ValueError("items in list must be either 0 or 1 valued integers")
            self.data[i] = bit

    def init_from_int(self, integer: int, int_size=DEFAULT_MAX_INT_BITS):
        tmp_data = ([int(bit) for bit in f"{integer:b}"])[::-1]

        # expand int_size if too small
        if int_size < len(tmp_data):
            int_size = ceil(len(tmp_data)/DEFAULT_BYTE_SIZE) * DEFAULT_BYTE_SIZE

        self.data = [0 for _ in range(int_size)]
        for i, v in enumerate(tmp_data):
            self.data[i] = v

    def byte_to_bits(self, single_byte)->list:
        tmp_data = ([int(bit) for bit in f"{int(single_byte):b}"])[::-1]

        bit_list = [0 for _ in range(DEFAULT_BYTE_SIZE)]

        for i, v in enumerate(tmp_data):
            bit_list[i] = v

        if len(bit_list) != 8:
            ValueError(f"bit_list ({len(bit_list)} value) len != 8")

        return bit_list

    def init_from_bytearray(self, bytes: bytearray):
        self.data = []
        for byte in bytes[::-1]:
            self.data.extend(iter(self.byte_to_bits(byte)))
        if (len(bytes) * 8) != len(self.data):
            raise ValueError(f"Expecting {(len(bytes) * 8)} bits, got {len(self.data)}")

    def to_int(self):
        if not self.data:
            raise ValueError("bitarray has no bits - can't convert to int")

        base_2_power = 1
        int_value = 0
        for bit in self.data:
            int_value += base_2_power * bit
            base_2_power *= 2

        return int_value

    def eight_bits_to_int(self, bits:list)->int:
        if len(bits) != 8:
            raise ValueError(f"more bits than will fit in a byte: {len(bits)} - {bits}")

        base_2_power = 1
        int_value = 0

        for bit in bits:
            int_value += base_2_power * bit
            base_2_power *= 2

        if int_value > 255:
            raise ValueError(f"Max int value for byte exceeded: {int_value} - {bits}")

        return int_value

    def to_bytearray(self):
        if not self.data:
            # Either None or [] no items in list then
            # then return empty bytearray object
            return bytearray()

        # bytes ordered least significant to most significant
        chunks = list(batched(self.data, 8))

        if len(chunks) != len(self.data) / 8:
            raise ValueError(
                f"chunked bit list ({len(chunks)} items) doesn't match bit list ({len(self.data)} items)"
            )

        # reverse chunk (list of 8 bits) list so that most significant comes first - network byte order
        # bytes ordered most significant to least significant
        chunks = list(chunks)[::-1]
        bytearray_value = bytearray()

        for chunk in chunks:
            bytearray_value.append(self.eight_bits_to_int(chunk))

        return bytearray_value

    def to_list(self)->list:
        return list(self.data)

















    # trick to keep Code from freaking out at the bottom of this file.
    def thing(self):
        ...
