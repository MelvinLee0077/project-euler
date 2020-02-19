import time 
def f(n):
	i = 2
	result = 0
	while i < n:
		if isPrime(i):
			result += i
		i += 1
	return result

def isPrime(n):
	i = 2
	while i*i <= n:
		if n % i == 0:
			return False
		i += 1
	return True
	
start = time.time()
print(f(2000000))
end = time.time()
print(end-start)