def f(n):
	i = 2
	while i < n:
		while n % i == 0:
			n /= i
		i += 1
	return i

print(f(600851475143))