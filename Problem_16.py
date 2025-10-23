# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


n = str(2**1000)
sum_of_digits = 0
for number in n: 
	sum_of_digits += int(number)

print(sum_of_digits)

# print(sum(int(digit) for digit in str(2**1000))) <- this is faster (16ms)
