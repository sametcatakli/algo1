from myList import *

print(map(math.sqrt, []))
print(map(math.sqrt, [2.0, 4.0, 6.0, 100.0]))
print(map(str.upper, ('hello')))
print(filter(is_prime, range(20)))
print(filter(str.isalpha, ('r2d2')))
print(reduce(math.pow, [2, 2]))
print(reduce(math.pow, [2, 3, 4]))

print(prime_numbers(2))
print(prime_numbers(12))

print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(33))

print(insert([], 1))
print(insert(list(range(6)), -1))
print(insert(list(range(6)), 3))
print(insert(list(range(6)), 10))

print(produit_matriciel([[2, 0, 1], [3, 6, 2]], [[1, 5], [2, 6], [3, 7]]))