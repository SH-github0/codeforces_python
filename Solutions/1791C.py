t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	s = input()
	answer = n % 2
	for i in range(n//2):
		if (s[i] == s[-i-1]):
			answer = n - 2 * i
			break
	print(answer)
