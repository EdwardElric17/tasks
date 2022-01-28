mas1 = []
mas = ''
point = ''
lst = ''
maxi = ''
max_count = 0
with open('06.txt', 'r') as inf:
	for line in inf:
		mas1.append(line.strip())
for i in range(len(mas1)):
	for j in mas1:
		mas += j[i]
	for item in mas:
		maxi =  