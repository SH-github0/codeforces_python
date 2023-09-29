import math

t = int(input())
while (t > 0):
	t -= 1
	a, b, c = map(int, input().split())
	diff = math.ceil(abs(a - b)/2)
	ans = (diff + c - 1) // c
	print (ans)
