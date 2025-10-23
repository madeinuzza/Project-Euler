# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math 

factorize = 600851475143
factors = []

for number in range((int(math.sqrt(factorize)) + 1), 1, -1): # range function: range(start, stop, step)  
	if factorize % number == 0:
		number_is_prime = True
		for i in range(2, (int(math.sqrt(number)) +1)): 
			if number % i == 0: 
				# then the number is not prime 
				number_is_prime = False
				break 
		if number_is_prime == True: 	
			largest_prime_factor = number 
			factors.append(number)
			break

print(largest_prime_factor) 
print(factors)

