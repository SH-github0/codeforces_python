t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	s = input()
	solved = {}
	answer = 0
	for si in s:
		if si in solved:
			answer += 1
		else:
			answer += 2
			solved[si] = True
	print(answer)
