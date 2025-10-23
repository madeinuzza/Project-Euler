# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

import math 

def is_it_prime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False 
	return True

number_of_primes = 0
for n in range(2, 10000000):
	x = is_it_prime(n)
	number_of_primes += x 
	if number_of_primes == 10001:
		print("the 10001st prime number is: ", n)
		break

print("number of primes: ", number_of_primes)

