t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	a = list(map(int, input().split()))
	a.sort()
	cost = 0
	for i in range(n//2):
		cost += a[-1-i] - a[i]
	print (cost)
