def f(upper):
	largest_chain = 0
	result = 0
	while upper > 0:
		chain = 0
		v = upper
		while v > 1:
			if isEven(v):
				v = v/2
			else:
				v = (3*v+1)
			chain += 1
		if chain > largest_chain:
			largest_chain = chain
			result = upper
		upper -= 1
	return result, largest_chain

def isEven(n):
	if n % 2 == 0:
		return True
	return False

print(f(1000000))