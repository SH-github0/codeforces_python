t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	a = list(map(int, input().split()))
	answer = True
	for i in range(n):
		if (a[i] % 2 == 1):
			answer = not answer
	if (answer):
		print("YES")
	else:
		print("NO")
