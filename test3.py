di = ['Faerun', 'Norrath', 'Tristram', 'AlphaCentauri', 'Arbre', 'Snowdin', 'Tambi', 'Straylight']
ti = []
mas = []
length = 0
long = 0
with open('08.txt', 'r') as inf:
    for line in inf:
        mas.append(line.strip().split())
print(mas)
for i in di:
    ti = []
    length = 0
    for n in di:
        ti.append(n)
    ti.remove(i)
    for j in ti:
        for k in range(len(mas)):
            if (mas[k][0] == i and mas[k][2] == j):
                length += int(mas[k][4])
                i = mas[k][2]
                break
            if (mas[k][2] == i and mas[k][4] == j):
                length += int(mas[k][4])
                i = mas[k][0]
                break
    if length > long:
        long = length
print(long)