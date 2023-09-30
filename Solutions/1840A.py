t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	s = input()
	ans = ""
	i = 0
	j = 1
	while (i < n and j < n):
		ans += s[i]
		while (s[j] != s[i] and j < n):
			j += 1
		i = j + 1
		j = i + 1
	print (ans)
