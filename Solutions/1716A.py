t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	ans = 0
	if (n == 1):
		ans = 2
	elif (n % 3 == 0):
		ans = n // 3
	else:
		ans = n//3 + 1
	print(ans)
