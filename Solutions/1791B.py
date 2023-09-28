t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	s = input()
	x = 0
	y = 0
	answer = "NO"
	for i in range(n):
		if (s[i] == 'L'):
			x -= 1
		elif (s[i] == 'R'):
			x += 1
		elif (s[i] == 'U'):
			y += 1
		else:
			y -= 1
		if (x == 1 and y == 1):
			answer = "YES"
			break
	print(answer)
