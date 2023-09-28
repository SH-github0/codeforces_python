t = int(input())
while (t > 0):
	t -= 1
	ans = ""
	for i in range(8):
		line = input()
		for j in range(8):
			if (line[j] != '.'):
				ans += line[j]
	print(ans)
