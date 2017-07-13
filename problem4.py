def is_palindrome(n):
	"""Returns whether a given number is a palindrome"""
	string = str(n)
	return string == string[::-1]

def main():
	"""Returns the largest number made up of two 3 digit numbers and is palindrome"""
	result = 0
	for i in range(999, 99, -1):
		for j in range(i, 99, -1):
			if is_palindrome(i * j):
				if (i * j) > result:
					result = i * j
	return result

print(main())