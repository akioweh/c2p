import timeit
from array import array
from itertools import compress
from math import isqrt
from typing import Iterator
from collections import Counter


def primes(n):
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


# fast (<< 1 sec) up to 1e7... ~2x speed of primes(n)
def primes2(n: int) -> list[int]:
    assert n > 1
    false = array('B', b'\x00')
    sieve = array('B', b'\x01') * (n // 2)
    for i in range(3, isqrt(n - 1) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = false * ((n - i * i - 1) // (2 * i) + 1)
    res = list(compress(range(1, n, 2), sieve))
    res[0] = 2
    return res


def factors(n: int) -> Iterator[int]:
    for prime in primes(isqrt(n) + 1):
        while not n % prime:
            yield prime
            n //= prime
            if n == 1:
                return
    if n > 1:
        yield n


def factorization(n: int) -> dict[int, int]:
    return Counter(factors(n))


if __name__ == '__main__':
    N = 10 ** 7
    print(timeit.timeit(lambda: primes(N), number=1))
    print(timeit.timeit(lambda: primes2(N), number=1))
