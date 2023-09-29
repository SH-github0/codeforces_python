t = int(input())
while (t > 0):
	t -= 1
	r = 0
	c = 0
	middle = False
	found = False
	input()
	for row in range(8):
		this_row = input().split('#')
		if found:
			continue
		if len(this_row) == 3 and not middle and not found:
			middle = True
		elif len(this_row) == 2 and middle and not found:
			c = len(this_row[0]) + 1
			r = row + 1
			middle = False
			found = True
	print(r, c)
