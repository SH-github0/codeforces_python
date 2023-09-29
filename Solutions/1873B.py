t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	a = list(map(int, input().split()))
	min_index = 0
	for i in range(n):
		if (a[i] < a[min_index]):
			min_index = i
	a[min_index] += 1
	answer = 1
	for i in range(n):
		answer *= a[i]
	print (answer)
