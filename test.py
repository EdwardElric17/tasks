mas = []
m = []
length = 0
k = 0
point1 = ''
point2 = ''
ind1 = ''
ind2 = ''
maxi = 0
with open('08.txt', 'r') as inf:
    for line in inf:
        mas.append(line.strip().split())
print(mas)
for i in range(len(mas)):
    if int(mas[i][4]) > maxi:
        maxi = int(mas[i][4])
        point1 = mas[i][0]
        point2 = mas[i][2]
        k = i
mas.pop(k)
print(mas)
length += maxi
print(maxi)
print(point1)
print(point2)
maxi = 0
for i in range(len(mas)):
    if mas[i][0] == point1 or mas[i][0] == point2:
        if int(mas[i][4]) > maxi:
            maxi = int(mas[i][4])
            ind1 = mas[i][0]
            ind2 = mas[i][2]
            k = i
    if  mas[i][2] == point1 or mas[i][2] == point2:
        if int(mas[i][4]) > maxi:
            maxi = int(mas[i][4])
            ind1 = mas[i][2]
            ind2 = mas[i][0]
            k = i
length += maxi
mas.pop(k)
def long(mas, index1, index2):
    global k
    global length
    a = ''
    b = ''
    maxi = 0
    for i in range(len(mas)):
        if index1 in mas[i] or index2 in mas[i]:
            if int(mas[i][4]) > maxi:
                maxi = int(mas[i][4])
                a = mas[i][0]
                b = mas[i][2]
                k = i
    length += maxi
    mas.pop(k)
    if len(mas) != 0:
        long(mas, a, b)
print(length)