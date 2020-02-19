import time
def f(term):
	i = 2
	count = 0
	while 1:
		if isPrime(i):
			count += 1
			if count == term:
				return i
		i += 1

def isPrime(n):
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

start = time.time()
print(f(10001))
end = time.time()
print(end-start)