t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	even_sum = 0
	odd_sum = 0
	a = list(map(int, input().split()))
	for i in range(n):
		if a[i] % 2 == 0:
			even_sum += a[i]
		else:
			odd_sum += a[i]
	if (even_sum > odd_sum):
		print("YES")
		continue
	print("NO")
