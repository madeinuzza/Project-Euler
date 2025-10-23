# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

def compute_divisors_sum(n):
	divisors = []
	for i in range(1, int(n/2) + 1):
		if n % i == 0: 
			divisors.append(i)
	return sum(divisors)

# print(compute_divisors_sum(284))

amicable_pairs = []
amicable_numbers = set() # empty set!
for a in range(1, 10001):
	d_a = compute_divisors_sum(a)
	d_b = compute_divisors_sum(d_a)
	if d_b == a and a != d_a:
		amicable_numbers.add(a)
		amicable_numbers.add(d_a)
		amicable_pairs.append("(" + str(a) + "," + str(d_a) + ")")	

print(amicable_numbers)
print(amicable_pairs)
print("sum of amicable pairs =", sum(amicable_numbers))