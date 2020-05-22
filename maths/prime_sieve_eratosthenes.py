"""
Sieve of Eratosthenes

Input : n =10
Output: [2, 3, 5, 7]

Input : n = 20
Output: [2, 3, 5, 7, 11, 13, 17, 19]

you can read in detail about this at
https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


def prime_sieve_eratosthenes(num: int) -> list:
    """
    print the prime numbers up to n

    >>> prime_sieve_eratosthenes(10)
    [2, 3, 5, 7]
    >>> prime_sieve_eratosthenes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """

    primes = [True for i in range(num + 1)]
    p = 2

    while p * p <= num:
        if primes[p]:
            for i in range(p * p, num + 1, p):
                primes[i] = False
        p += 1

    return primes


if __name__ == "__main__":
    num = int(input())

    print(prime_sieve_eratosthenes(num))
