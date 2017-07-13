def main(n):
	"""Returns the sum of fibonacci numbers that are multiples of 3 or 5 upto a given point"""
	result = 0
	# Brute Force
	for i in range(n):
		if i % 3 == 0:
			result += i
		elif i % 5 == 0:
			result += i
	return result

print(main(1000))