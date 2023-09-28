t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	r1 = input()
	r2 = input()
	answer = "YES"
	for i in range(n):
		if ((r1[i] == 'R' and r2[i] != 'R') or (r2[i] == 'R' and r1[i] != 'R')):
			answer = "NO"
			break
	print(answer)
