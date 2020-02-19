# https://www.mathblog.dk/project-euler-problem-4/

def f(n):
	max_1 = int(str(9)*n)
	max_2 = max_1
	start = max_1
	factors = (0,0)
	largest = 0
	while max_1 > 0:
		max_2 = start
		while max_2 > 0:
			prod = max_1*max_2
			if isPalindrome(prod) and prod > largest:
				largest = max_1*max_2
				factors = (max_1,max_2)
			max_2 -= 1
		max_1 -= 1
	return largest,factors

def isPalindrome(value):
	tmp_value = value
	rev_value = ""
	if numberOfDigit(value) % 2 != 0:
		return False
	else:
		if str(value) == str(value)[::-1]:
			return True
		return False

def numberOfDigit(m):
	count = 0
	while m > 1:
		m /= 10
		count += 1
	return count

print(f(3))