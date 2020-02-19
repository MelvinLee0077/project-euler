def f(n):
	return abs(sum_of_square(n)-square_of_sum(n))

def sum_of_square(n):
	i = 1
	result = 0
	while i <= n:
		result += i*i
		i += 1
	return result

def square_of_sum(n):
	i = 1
	result = 0
	while i <= n:
		result += i
		i += 1
	return result**2

print(f(100))
