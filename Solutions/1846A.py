t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	ans = 0
	for i in range(n):
		a, b = map(int, input().split())
		if (a > b):
			ans += 1
	print(ans)
