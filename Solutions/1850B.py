t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	ans = 0
	best_quality = 0
	for i in range(n):
		a, b = map(int, input().split())
		if (a <= 10 and b > best_quality):
			ans = i + 1
			best_quality = b
	print(ans)
