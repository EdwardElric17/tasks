mas1 = []
mas = ''
point = ''
lst = ''
maxi = 0
max_count = 0
with open('06.txt', 'r') as inf:
    for line in inf:
        mas1.append(line.strip())
    mas = ''
    gty = set(mas1)
    for i in range(8):
        for j in mas1:
            mas += j[i]
        set_mas = set(mas)
print(mas)
print(set_mas)