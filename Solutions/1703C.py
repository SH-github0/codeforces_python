t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	a = list(map(int, input().split()))
	ans = 0
	for i in range(n):
		b, moves = input().split()
		b = int(b)
		change = 0
		for j in range(b):
			if moves[j] == 'U':
				change += 1
			else:
				change -= 1
		ans = (a[i] - change) % 10
		print(ans, end = " ")
	print()
