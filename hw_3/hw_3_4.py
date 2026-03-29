""" Homework 3 task 4 """


from __future__ import annotations


class BinaryNumber:
    """ Class of binary number"""
    def __init__(self, value: str) -> None:
        self.value = value

    def __and__(self, other: BinaryNumber) -> BinaryNumber:
        """ Method of logical AND, returns the binary instance"""
        max_len = max(len(self.value), len(other.value)) # complete to the same length
        a = self.value.zfill(max_len)
        b = other.value.zfill(max_len)
        result = ''.join('1' if x=='1' and y=='1' else '0' for x,y in zip(a,b))
        return BinaryNumber(result)

    def __or__(self, other: BinaryNumber) -> BinaryNumber:
        """ Method of logical OR, returns the binary instance"""
        max_len = max(len(self.value), len(other.value)) # complete to the same length
        a = self.value.zfill(max_len)
        b = other.value.zfill(max_len)
        result = ''.join('1' if x=='1' or y=='1' else '0' for x,y in zip(a,b))
        return BinaryNumber(result)

    def __xor__(self, other: BinaryNumber) -> BinaryNumber:
        """ Method of logical OR, returns the binary instance"""
        max_len = max(len(self.value), len(other.value)) # complete to the same length
        a = self.value.zfill(max_len)
        b = other.value.zfill(max_len)
        result = ''.join('1' if (x=='1') != (y=='1') else '0' for x,y in zip(a,b))
        return BinaryNumber(result)

    def __invert__(self) -> BinaryNumber:
        """ Method of logical NOT, returns the binary instance"""
        result = ''.join('0' if x=='1' else '1' for x in self.value)
        return BinaryNumber(result)

    def __repr__(self) -> str:
        """ Returns BinaryNumber`s representation """
        return f"{self.value}"


def main():
    """main def"""
    a = BinaryNumber("1110")   # 14
    b = BinaryNumber("1011")   # 11

    print("A      =", a)
    print("B      =", b)

    print("A AND B =", a & b)
    print("A OR B  =", a | b)
    print("A XOR B =", a ^ b)
    print("NOT A   =", ~a)
    print("NOT B   =", ~b)


if __name__ == "__main__":
    main()
