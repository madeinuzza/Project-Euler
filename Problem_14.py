# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz_sequence(n, size_of_sequence):
	if n == 1:
		return n, size_of_sequence 
	elif n % 2 == 0: 
		return collatz_sequence(int(n/2), size_of_sequence + 1)
	else: 
		return collatz_sequence(3*n +1, size_of_sequence +1)

# print(collatz_sequence(13, 1))

largest_sequence = 1
for i in range(1, 1000000):
	one, size_of_sequence = collatz_sequence(i, 1)
	if size_of_sequence > largest_sequence:
		largest_sequence = size_of_sequence
		starting_number = i

print(starting_number)
print("largest_sequence = ", largest_sequence)
