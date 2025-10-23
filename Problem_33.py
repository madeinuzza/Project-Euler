# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

from fractions import Fraction

#x = Fraction(10,20) + Fraction(10,20)
#print(x)

weird_fractions = set()

for i in range(1,10):
	for x in range(1, 10):
		for y in range(1, 10):
			nominator_1 = int(str(i) + str(x))
			denominator_1 = int(str(i) + str(y))
			nominator_2 = int(str(i) + str(x))
			denominator_2 = int(str(y) + str(i))
			nominator_3 = int(str(x) + str(i))
			denominator_3 = int(str(i) + str(y))
			nominator_4 = int(str(x) + str(i))
			denominator_4 = int(str(y) + str(i)) 
			if (Fraction(nominator_1, denominator_1) == Fraction(x, y)) and (nominator_1 != denominator_1): 
				weird_fractions.add(Fraction(nominator_1, denominator_1))
				print("x =", x, "y = ", y)
			if (Fraction(nominator_2, denominator_2) == Fraction(x, y)) and (nominator_2 != denominator_2):
				weird_fractions.add(Fraction(nominator_2, denominator_2))
				print("x =", x, "y = ", y)
			if (Fraction(nominator_3, denominator_3) == Fraction(x, y)) and (nominator_3 != denominator_3): 
				weird_fractions.add(Fraction(nominator_3, denominator_3))
				print("x =", x, "y = ", y)
			if (Fraction(nominator_4, denominator_4) == Fraction(x, y)) and (nominator_4 != denominator_4): 
				weird_fractions.add(Fraction(nominator_4, denominator_4))
				print("x =", x, "y = ", y)


print(weird_fractions)

product_of_fractions = 1
for fraction in weird_fractions:
	if fraction < 1: 
		product_of_fractions = product_of_fractions * fraction

print(product_of_fractions)


