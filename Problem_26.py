# Considering quadratics of the form:

# n^2 + an + b, where |a| < 1000 and |b| <= 1000 

# Find the product of the coefficients, a and b, 
# for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

import math 

for i in range(1,1):
	nothing = 0 

def is_it_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False 
    return True

maximum_number_of_primes = 0
for a in range(-999, 1000, 1):
	for b in range(-1000, 1000, 1):
		n = 0
		quadratic_form = int(n**2 + a*n + b)
		while quadratic_form > 0 and is_it_prime(quadratic_form) == True:
			n += 1 
			quadratic_form = int(n**2 + a*n + b)
		if n > maximum_number_of_primes: 
			maximum_number_of_primes = n 
			desired_a = a 
			desired_b = b

print(maximum_number_of_primes)
print(desired_b)
print(desired_a)
print(desired_b * desired_a)