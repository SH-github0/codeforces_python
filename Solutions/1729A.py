t = int(input())
while (t > 0):
	t -= 1
	a, b, c = map(int, input().split())
	t1 = a - 1
	t2 = abs(b - c) + c - 1
	ans = 3
	if (t1 < t2):
		ans = 1
	elif (t2 < t1):
		ans = 2
	print(ans)
