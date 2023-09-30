t = int(input())
while (t > 0):
	t -= 1
	n = int(input())
	s = input()
	melodies = set()
	for i in range(n - 1):
		melodies.add(s[i:i+2])
	print(len(melodies))
