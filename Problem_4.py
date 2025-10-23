# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

palindromes = {}
largest = 0
for i in range(10, 1000, 1):
	for j in range(10, 1000, 1):
		product = i*j 
		string_product = str(product)
		size_of_product = len(string_product)

		palindrome = True 
		for k in range(0, size_of_product -1,1):
			if string_product[k] != string_product[size_of_product - 1 - k]:
				palindrome = False
				break

		if palindrome == True: 
			palindromes[i*j] = [i,j]
			if i*j  > largest: largest = i*j

print(largest)
print(palindromes)


