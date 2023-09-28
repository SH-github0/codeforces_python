t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	a = list(map(int, input().split()))
	ans = 0
	curr = 0
	for i in range(n):
		if (a[i] == 1):
			if (curr > ans):
				ans = curr
			curr = 0
		else:
			curr += 1
	if (curr > ans):
		ans = curr
	print(ans)
