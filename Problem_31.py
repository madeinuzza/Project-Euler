# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

# It is possible to make £2 in the following way:

#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

# How many different ways can £2 be made using any number of coins?



# I will create a list with all possible multiples of 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p) less than 200p

1p = [n for n in range(1, 201)]
2p = [2*n for n in range(1, int(200/2)+1)]
