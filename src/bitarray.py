# bitarray/src/bitarray.py

from typing import Self
from itertools import batched
from math import ceil

DEFAULT_MAX_INT_BITS = 64
DEFAULT_BYTE_SIZE = 8

class bitarray():
    # 'data' is an array of integers where the items in the array
    # are constrained to be either 0 or 1.
    # These are arranged so that the most significant bits (bigger values)
    # are indexed with higher positional values than less significant bits.
    # When converting to/from 'bytearray` type values using bitarray.to_bytearray/bitarray.from_bytearray,
    # this implementation assumes network byte order (e.g. network order) is being used.
    # See https://en.wikipedia.org/wiki/Endianness#Networking for a description of network order.
    data = []

    def __init__(
            self,
            bits:(Self | list | int | bytearray | str),
            max_int_bits:int=DEFAULT_MAX_INT_BITS
        ):
        if isinstance(bits, list):
            self.init_from_list(bits)

        elif isinstance(bits, int):
            self.init_from_int(bits)

        elif isinstance(bits, bytearray):
            self.init_from_bytearray(bits)

        elif isinstance(bits, type(self)):
            self.data = list(bits.data)

        elif bits is not None:
            raise ValueError(f"Invalid Value Type ({type(bits)}) for bits")

    def init_from_list(self, bits:list):
        # list must contain only ints with values of 1 or 0
        for i in bits:
            if not isinstance(i, int) or i not in [0, 1]:
                raise ValueError("list elements must be integers with a value of 0 or 1")
        self.data = bits

    # +	__add__(self, other)	Addition
    def __add__(self, rhs:(Self | bytearray | int)) -> Self:
        raise NotImplementedError()

    def __radd__(self, lhs:(Self | bytearray | int)) -> Self:
        raise NotImplementedError()

    # -	__sub__(self, other)	Subtraction
    def __sub__(self, rhs:(Self | bytearray | int)) -> Self:
        raise NotImplementedError()

    def __rsub__(self, lhs:(Self | bytearray | int)) -> Self:
        raise NotImplementedError()

    # *	__mul__(self, other)	Multiplication
    def __mul__(self, rhs:(Self | bytearray | int)) -> Self:
        raise NotImplementedError

    def _rmul__(self, lhs:(Self | bytearray | int)) -> Self:
        raise NotImplementedError()

    # /	__truediv__(self, other)	Division
    def __truediv__(self, rhs:(Self | bytearray | int)) -> Self:
        raise NotImplementedError

    def __rtruediv__(self, lhs:(Self | bytearray | int)) -> Self:
        raise NotImplementedError()

    # ==	__eq__(self, other)	Equality
    def __eq__(self, rhs:(Self | bytearray | int)) -> Self:
        if isinstance(rhs, (bytearray, int)):
            rhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        if len(self) != len(rhs):
            raise ValueError("AND operations require the same number of bits in both values.")

        return all(rhs[i] == self.data[i] for i, v in enumerate(rhs, start=0))

    def __req__(self, lhs:(Self | bytearray | int)) -> Self:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        if len(self) != len(lhs):
            raise ValueError("== operations require the same number of bits in both values.")

        return [self.data[i] & v for i, v in enumerate(lhs, start=0)]

    # <	__lt__(self, other)	Less than
    def __lt__(self, rhs:(Self | bytearray | int)) -> Self:
        raise NotImplementedError()

    def __rlt__(self, lhs:(Self | bytearray | int)) -> Self:
        raise NotImplementedError()

    # &	__and__(self, other)	    Bitwise AND
    def __and__(self, rhs:(Self | bytearray | int)) -> Self:
        if isinstance(rhs, (bytearray, int)):
            lhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        if len(self) != len(rhs):
            raise ValueError("AND operations require the same number of bits in both values.")

        return [self.data[i] & v for i, v in enumerate(rhs, start=0)]

    def __rand__(self, rhs:(Self | bytearray | int)) -> Self:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        if len(self) != len(lhs):
            raise ValueError("OR operations require the same number of bits in both values.")

        return [v & self.data[i] for i, v in enumerate(lhs, start=0)]

    # |	__or__(self, other)	        Bitwise OR
    def __or__(self, rhs:(Self | bytearray | int)) -> Self:
        if isinstance(rhs, bytearray) or isinstance(lhs, int):
            lhs = (type(self))(lhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")
        
        if len(self) != len(lhs):
            raise ValueError("OR operations require the same number of bits in both values.")
        
        return [self.data[i] | v for i, v in enumerate(rhs, start=0)]

    def __ror__(self, lhs:(Self | bytearray | int)) -> Self:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        if len(self) != len(lhs):
            raise ValueError("OR operations require the same number of bits in both values.")

        return [v | self.data[i] for i, v in enumerate(lhs, start=0)]

    # ^	__xor__(self, other)	    Bitwise XOR
    def __xor__(self, rhs:(Self | bytearray | int)) -> Self:
        if isinstance(rhs, (bytearray, int)):
            lhs = (type(self))(rhs)

        if not isinstance(rhs, type(self)):
            raise TypeError(f"argument 'rhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        if len(self) != len(rhs):
            raise ValueError("XOR operations require the same number of bits in both values.")

        return [v ^ self.data[i] for i, v in enumerate(rhs, start=0)]

    def __rxor__(self, lhs:(Self | bytearray | int)) -> Self:
        if isinstance(lhs, (bytearray, int)):
            lhs = (type(self))(lhs)

        if not isinstance(lhs, type(self)):
            raise TypeError(f"argument 'lhs' must be one of '{type(self)}' or 'int' or 'bytearray'")

        if len(self) != len(lhs):
            raise ValueError("XOR operations require the same number of bits in both values.")

        return [v ^ self.data[i] for i, v in enumerate(lhs, start=0)]

    # ~	__invert__(self)	        Bitwise NOT (Unary)
    def __invert__(self) -> Self:
        return type(self)([1 if n == 0 else 0 for n in self.data])

    # <<	__lshift__(self, other)	Left Shift
    def __lshift__(self, rhs:int) -> Self:
        if not isinstance(rhs, int):
            raise TypeError("argument 'rhs' must be of type 'int'")
        new_instance_copy = type(self)(self.data)
        return (new_instance_copy.data.insert(0, rhs))[:-rhs]

    # >>	__rshift__(self, other)	Right Shift
    def __rshift__(self, rhs:int) -> Self:
        return type(self)((self.data[:-rhs]).insert(0, 0))

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index:(int | slice)) -> (int | list):
        if isinstance(index, (slice, int)):
            # start, stop, step = index.indices(self.__len__())
            # return [bit for bit in self.data[start, stop, step]]
            return self.data[index]

        raise ValueError(f"Invalid Index of type {type(index)}")

    def __setitem__(self, index:(int | slice), value:(int | list)):
        if isinstance(index, slice) and isinstance(value, list) and hasattr(value, "__iter__"):
            self.data[index] = value
            return
        elif isinstance(index, int) and isinstance(value, int):
            self.data[index] = value
            return

        raise ValueError(f"Invalid Value Type ({type(value)}) for 'value' when slicing or indexing")

    def __delitem__(self, index:(int | slice)):
        if isinstance(index, (slice, int)):
            del self.data[index]
            return

        raise ValueError(f"Invalid Value Type ({type(value)}) for 'value' when slicing or indexing")

    def __repr__(self)->str:
        return f"{type(self)}: {self.data}"

    def insert(self, index:(int | slice), value:(int | slice)):
        self.data.insert(index, value)
        return

    def append(self, value:(int | list)):
        self.data.insert(len(self), value)

    def extend(self, value:list):
        self.data.extend(value)

    def clear(self):
        del self.data[:]

    def reverse(self):
        self.data.reverse()

    def init_from_list(self, bit_list: list):
        for bit in bit_list:
            if not isinstance(bit, int) or bit not in [0, 1]:
                raise ValueError("items in list must be either 0 or 1 valued integers")
            self.data = list(bit_list)

    def init_from_int(self, integer: int, int_size=DEFAULT_MAX_INT_BITS):
        # for bit in (f"{integer:0{int_size}b}")[::-1]:
        #     self.data.append(int(bit))
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

        return bit_list

    def init_from_bytearray(self, bytes: bytearray):
        for byte in bytes[::-1]:
            for bit in self.byte_to_bits(byte):
                self.data.append(bit)

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
        base_2_power = 1
        int_value = 0
        for bit in bits:
            int_value += base_2_power * bit
            base_2_power *= 2
        return int_value

    def to_bytearray(self):
        # least significant to most significant
        chunks = list(batched(self.bits, 8))
        # reverse list so that most significant comes first - network byte order
        chunks.reverse()
        bytearray_value = bytearray()
        for chunk in chunks:
            chunk_value = self.eight_bits_to_int(chunk)
            bytearray_value.append(chunk_value)
        
        return bytearray_value



















    # trick to keep Code from freaking out at the bottom of this file.
    def thing(self):
        ...
