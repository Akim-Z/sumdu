mas = []
for j in range(7):
	row = []
	for i in range(7):
		x = 7 - i - j
		if x < 0: 
			x = 0
		row.append(x)
	mas.append(row)	

for row in mas:
	print(row)
