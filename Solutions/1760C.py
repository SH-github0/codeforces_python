t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	s = list(map(int, input().split()))
	strongest = s[0]
	second_strongest = s[1]
	if second_strongest > strongest:
		strongest, second_strongest = second_strongest, strongest
	for i in range(2, n):
		if s[i] > strongest:
			second_strongest = strongest
			strongest = s[i]
		elif s[i] > second_strongest:
			second_strongest = s[i]
	for i in range(n):
		if (s[i] == strongest):
			print (s[i] - second_strongest, end = " ")
		else:
			print (s[i] - strongest, end = " ")
	print()
