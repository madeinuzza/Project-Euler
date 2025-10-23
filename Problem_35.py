# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?


from itertools import permutations as p
import math 

def is_it_prime(n):
	for i in range(2, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False 
	return True

circular_primes = [] # the list will consist of tuples, where each entry is a tuple consisting of the digits of the prime number 
for n in range(2, 1000000):
	if is_it_prime(n) == True: 
		permut = list(p(str(n)))
		for number in permut:
			string_number = ""
			for digit in number:
				string_number += digit
			integer_number = int(string_number)
			if is_it_prime(integer_number) == True:
				circular_prime = True
			else:
				circular_prime = False
				break 
		if circular_prime == True:
			circular_primes.append(n)
			print(n)

print(circular_primes) 
print(len(circular_primes))


# milionth_perm = 0
# list2 = []
# def perm(list):
#     for chars in p(list):
#         list2.append(chars)
#         if len(list2) == 1_000_000:
#             milionth_perm = chars
#             break
#     return milionth_perm

# print(perm([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))

