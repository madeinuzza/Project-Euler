# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

# 012   021   102   120   201   210

# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# Test case, n = 4

# counter = 0
# permutations = []
# for i in range(0,4):
# 	for j in range(0,4):
# 		if j == i: continue 
# 		for k in range(0,4):
# 			if k == j or k == i: continue
# 			for a in range(0,4):
# 				if a == j or a == i or a == k: continue
# 				number = str(i) + str(j) + str(k) + str(a) 
# 				counter += 1
# 				permutations.append(number)
# print(permutations)
# print(counter)

counter = 0
permutations = []
for i in range(0,10):
	for j in range(0,10):
		if j == i: continue 
		for k in range(0,10):
			if k == j or k == i: continue
			for a in range(0,10):
				if a == j or a == i or a == k: continue
				for b in range(0,10):
					if b == a or b == i or b == k or b == j: continue
					for c in range(0,10):
						if c == i or c == j or c == k or c == a or c == b: continue
						for d in range(0,10):
							if d == i or d == j or d == k or d == a or d == b or d == c: continue
							for e in range(0,10):
								if e == i or e == j or e == k or e == a or e == b or e == c or e == d: continue
								for f in range(0,10):
									if f == i or f == j or f == k or f == a or f == b or f == c or f == d or f == e: continue
									for g in range(0,10):
										if g == i or g == j or g == k or g == a or g == b or g == c or g == d or g == e or g == f: continue
										number = str(i) + str(j) + str(k) + str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g)
										counter += 1 
										if counter == 1000000:
											print(number)
											break
										permutations.append(number)

#print(permutations)

# # FROM COMMENTS 
# from itertools import permutations as p

# milionth_perm = 0
# list2 = []
# def perm(list):
#     for chars in p(list):
#         list2.append(chars)
#         if len(list2) == 1_000_000:
#             milionth_perm = chars
#             break
#     return milionth_perm

# print(perm([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
