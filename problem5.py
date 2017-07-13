def main():
	"""Returns the smallest number that is divisible by every number from 0 to 20"""
	start = 20
	# We only need to check multiples of 20 as it must be divisible by 20
	found = False
	while found == False:
		found = True
		for i in range(20, 1, -1):
			if start % i != 0:
				found = False
				start += 20
				break
		
	return start


print(main())
	