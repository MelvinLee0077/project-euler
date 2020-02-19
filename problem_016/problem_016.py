def f():
	result = 0
	value = 2**1000
	while value:
		result += value % 10
		value //= 10
	return result

def f2():
	result = 0
	value = 2**1000
	for ch in str(value):
		result += int(ch)
	return result

print(f())