rg = range(101)

for i in rg:
	if 0 == i%7:
		continue
	if 7 == i%10:
		continue
	if 7 == i//10:
		continue
	print(i)