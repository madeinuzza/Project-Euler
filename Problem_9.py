# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 							a^2 + b^2 = c^2

# For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

def pythagorean(a,b,c):
	if a**2 + b**2 == c**2:
		return True
	return False

def sum(a,b,c):
	if a + b + c == 1000:
		return True
	return False

for c in range(1, 1000):
	for b in range(1, c):
		for a in range(1, b):
			if pythagorean(a,b,c) and sum(a,b,c):
				print("a = ", a, "b = ", b, "c = ", c)
				print("a*b*c = ", a*b*c)
				