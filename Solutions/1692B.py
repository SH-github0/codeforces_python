t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	a = set(map(int, input().split()))
	ans = len(a)
	if (ans - n) % 2 == 1:
		ans -= 1
	print(ans)
