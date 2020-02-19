def f(n):
	allArray = []
	with open("problem_011a.txt", "r") as file:
		processedData = file.read().split("\n")
		for row in processedData:
			rowArray = []
			for value in row.split(" "):
				rowArray.append(int(value))
			allArray.append(rowArray)
	file.close()
		
	largest_prod = allArray[0][0] * allArray[0][1] * allArray[0][2] * allArray[0][3]
	a = 0
	b = 0
	c = 0
	d = 0
	# top down 
	for row in range(len(allArray)-n+1):
		for i in range(len(allArray[row])):
			if i < len(allArray[row]) - n + 1:
				origin = allArray[row][i]
				right_1 = allArray[row][i+1]
				right_2 = allArray[row][i+2]
				right_3 = allArray[row][i+3]
				bottom_1 = allArray[row+1][i]
				bottom_2 = allArray[row+2][i]
				bottom_3 = allArray[row+3][i]
				diag_right_1 = allArray[row+1][i+1]
				diag_right_2 = allArray[row+2][i+2]
				diag_right_3 = allArray[row+3][i+3]

				prod_horizontal = origin * right_1 * right_2 * right_3
				prod_vertical = origin * bottom_1 * bottom_2 * bottom_3
				prod_diag_right = origin * diag_right_1 * diag_right_2 * diag_right_3

				if prod_horizontal >= prod_vertical and prod_horizontal >= prod_diag_right:
					if prod_horizontal > largest_prod:
						largest_prod = prod_horizontal
						a = origin
						b = right_1
						c = right_2
						d = right_3
				elif prod_vertical >= prod_horizontal and prod_vertical >= prod_diag_right:
					if prod_vertical > largest_prod:
						largest_prod = prod_vertical
						a = origin
						b = bottom_1
						c = bottom_2
						d = bottom_3
				else:
					if prod_diag_right > largest_prod:
						largest_prod = prod_diag_right
						a = origin
						b = diag_right_1
						c = diag_right_2
						d = diag_right_3
			else:
				origin = allArray[row][i]
				bottom_1 = allArray[row+1][i]
				bottom_2 = allArray[row+2][i]
				bottom_3 = allArray[row+3][i]
				prod_vertical = origin * bottom_1 * bottom_2 * bottom_3
				if prod_vertical > largest_prod:
					largest_prod = prod_vertical
					a = origin
					b = bottom_1
					c = bottom_2
					d = bottom_3

	# LTR diagonal (bottom up)
	for row in range(len(allArray)-1, n+1, -1):
		for i in range(len(allArray[row])-n+1):
			origin = allArray[row][i]
			diag_left_1 = allArray[row-1][i+1]
			diag_left_2 = allArray[row-2][i+2]
			diag_left_3 = allArray[row-3][i+3]

			prod_diag_left = origin * diag_left_1 * diag_left_2 * diag_left_3
			if prod_diag_left >= largest_prod:
				largest_prod = prod_diag_left
				a = origin
				b = diag_left_1
				c = diag_left_2
				d = diag_left_3

	return largest_prod, a,b,c,d

print(f(4))