# https://www.tutorialspoint.com/python3/bitwise_operators_example.htm


def binary_or(a: int, b: int):
    """
    Take in 2 integers, convert them to binary, and return a binary number that is the
    result of a binary or operation on the integers provided.

    >>> binary_or(25, 32)
    '0b111001'
    >>> binary_or(37, 50)
    '0b110111'
    >>> binary_or(21, 30)
    '0b11111'
    >>> binary_or(58, 73)
    '0b1111011'
    >>> binary_or(0, 255)
    '0b11111111'
    >>> binary_or(0, 256)
    '0b100000000'
    >>> binary_or(0, -1)
    Traceback (most recent call last):
        ...
    ValueError: the value of both input must be positive
    >>> binary_or(0, 1.1)
    Traceback (most recent call last):
        ...
    TypeError: 'float' object cannot be interpreted as an integer
    >>> binary_or("0", "1")
    Traceback (most recent call last):
        ...
    TypeError: '<' not supported between instances of 'str' and 'int'
    """
    if a < 0 or b < 0:
        raise ValueError("the value of both input must be positive")
    if isinstance(a, float) or isinstance(b, float):
        raise TypeError("'float' object cannot be interpreted as an integer")

    result = []
    append = result.append
    while a or b:
        # comparing every bit of a and b, finding bits through division method.
        # https://en.wikipedia.org/wiki/Binary_number#Conversion_to_and_from_other_numeral_systems
        append(str(int((a % 2) or (b % 2))))
        a //= 2
        b //= 2
    append('0b')
    return ''.join(reversed(result))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
