# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math 

def is_it_prime(n):
	for j in range(2, int(math.sqrt(n)) + 1):
		if n % j == 0:
			return False 
	return True

count = 0
for n in range(2, 2000000):
	if is_it_prime(n) == True:
		count += n 

print(count)


