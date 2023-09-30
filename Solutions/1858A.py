t = int(input())
while (t > 0):
	t -= 1
	a, b, c = map(int, input().split())
	ans = ""
	if (c % 2 == 0):
		if (a > b):
			ans = "First"
		else:
			ans = "Second"
	else:
		if (b > a):
			ans = "Second"
		else:
			ans = "First"
	print (ans)
