def main():
	"""Returns the sum of even fibonacci numbers up to 4000000"""
	result = 0
	# Since every third fibonacci is even, we can calculate this and add to result
	first, second, third = 1, 1, 2
	while third < 4000000:
		result += third
		first = third + second
		second = first + third
		third = first + second
	return result
print(main())