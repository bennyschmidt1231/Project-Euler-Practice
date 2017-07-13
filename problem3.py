import math

def main(n):
	"""Calculates the largest prime factor of a given number"""
	result = 0
	factors = []
	# Every prime factor must be less than the square root
	square_root = math.sqrt(n)
	square_root = int(square_root // 1)
	for i in range(3, square_root + 1):
		if (n % i) == 0:
			prime = True
			# Check found number is a prime factor
			for num in factors:
				if (i % num) == 0:
					prime = False
					break
			if prime == True:
				factors.append(i)
				result = i
	return result

print(main(600851475143))