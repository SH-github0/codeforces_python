t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	s = input()
	answer = 0
	for i in range(n):
		d = ord(s[i]) - ord('a') + 1
		if d > answer:
			answer = d
	print(answer)
