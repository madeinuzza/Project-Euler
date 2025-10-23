# The sum of the squares of the first ten natural numbers is,
# 			1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,
#			(1 + 2 + ... + 10)^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

# I will be using the following formula: (\sum_{n=1}^{1000} a_i )^2 = \sum_{n=1}^{1000} (a_n)^2 + 2 (\sum_{i<j} a_i a_j)

difference = 0
for i in range(1,101):
	for j in range(1,i):
		#print("i*j= ", i*j)
		difference += i*j 

print(difference*2) 

