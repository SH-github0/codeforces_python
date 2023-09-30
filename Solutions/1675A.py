t = int(input())
while (t > 0):
	t -= 1
	a, b, c, x, y = map(int, input().split())
	ans = "NO"
	unfed_dogs = max(0, x - a)
	unfed_cats = max(0, y - b)
	if (unfed_dogs + unfed_cats <= c):
		ans = "YES"
	print (ans)
