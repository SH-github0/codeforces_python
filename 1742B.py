t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	a = list(map(int, input().split()))
	amap = {}
	answer = True
	for i in range(n):
		if (a[i] in amap):
			answer = False
			break
		else:
			amap[a[i]] = True
	if (answer):
		print("YES")
	else:
		print("NO")
