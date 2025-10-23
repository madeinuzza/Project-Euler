# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import math


for i in range(2, math.factorial(20)):
	divisible = True
	for j in range(2, 21):
		if i % j != 0:	
			divisible = False
			break 
	if divisible == True:
		print(i)
		break 