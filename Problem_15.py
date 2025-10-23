# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# RRDD RDRD RDDR DRRD DRDR DDRR (R = right, D = down)
# How many such routes are there through a 20×20 grid?

# I use the binomial coefficient: (n over k) = n! / (k! (n-k)!)


def factorial(n):
	if n == 1: 
 		return n
	else: 
 		return n*factorial(n-1)

routs = factorial(40) / (factorial(20)*factorial(20)) 
print("number of routs = ", routs)