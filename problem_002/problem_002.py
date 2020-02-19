def f(limit):
	prev_0 = 1
	prev_1 = 2	
	result = 2 
	while prev_0 + prev_1 < limit:
		tmp = prev_0 + prev_1	
		if tmp % 2:
			result += tmp
		prev_0 = prev_1
		prev_1 = tmp
	return result
print(f(4000000))