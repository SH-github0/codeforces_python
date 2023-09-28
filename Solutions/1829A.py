t = int(input())
c = "codeforces"
while (t > 0):
	t -= 1
	answer = 0
	s = input()
	for i in range(10):
		if (c[i] != s[i]):
			answer += 1
	print(answer)
