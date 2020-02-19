import time

def f(upper):
	i = 0
	sum = 0
	while i < upper:
		if i % 3 == 0 or i % 5 == 0:
			sum += i
		i += 1
	return sum

start = time.time()
print(f(1000))
end = time.time()
print(end-start)
