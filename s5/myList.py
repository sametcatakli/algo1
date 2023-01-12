import math


def map(fct, t):
    res = []
    for i in range(len(t)):
        res.append(fct(t[i]))
    return res


def filter(fct, t):
    res = []
    for i in t:
        if fct(i):
            res.append(i)
    return res


def reduce(fct, t):
    acc = t[0]
    for i in t[1:]:
        acc = fct(acc, i)
    return acc


def prime_numbers(n):
    if n == 0:
        return []
    else:
        primes = [2]
        candidate = 3
        while len(primes) < n:
            is_prime = True
            for prime in primes:
                if prime > math.sqrt(candidate):
                    break
                if candidate % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(candidate)
            candidate += 2
    return primes


def is_prime(n):
    deno = []
    for i in range(n + 1):
        if i != 0:
            if str((n / i))[-1] == "0":
                deno.append(i)
    return len(deno) == 2


def insert(seq, n):
    x = len(seq)
    seq.append(n)
    while n < seq[x - 1] and x > 0:
        a = seq[x - 1]
        seq[x - 1] = n
        seq[x] = a
        x -= 1

    return seq


def produit_matriciel(A, B):
    C = []
    ma = len(A)
    na = len(A[0])

    mb = len(B)
    nb = len(B[0])

    # pas réussi à faire


