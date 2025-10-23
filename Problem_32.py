# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

set_of_products = set()
pan_list = []
for x in range(1, 10**4):
	for y in range(1, 10**4):
		z = x * y 
		string_of_digits = str(x) + str(y) + str(z)
		sum_of_digits = 0
		if ("0" in str(x)) or ("0" in str(y)) or ("0" in str(z)): sum_of_digits += 9
		for i in range(1, 10):
			if str(i) in string_of_digits: sum_of_digits += 1
			if len(string_of_digits) > 9: sum_of_digits += 9
		if sum_of_digits  == 9:
			pan_list.append(x)
			pan_list.append(y)
			pan_list.append(z)
			set_of_products.add(z)

print(set_of_products)
print(pan_list)
print(sum(set_of_products))