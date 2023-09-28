t = int(input())
PI = "314159265358979323846264338327"
while (t > 0):
	t -= 1
	s = input()
	ans = 0
	i = 0
	for i in range(len(s)):
		if (s[i] != PI[i]):
			break
		ans += 1
	print(ans)
