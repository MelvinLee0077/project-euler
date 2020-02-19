def f(n):
	with open("problem_013a.txt","r") as file:
		processedData = file.read().split("\n")
		result = 0
		for row in processedData:
			result += float(row)
	file.close()
	return str(result).replace(".","")[:n]

print(f(10))