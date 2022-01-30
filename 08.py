mas = []
m = []
lenh = 0
a = 0
point1 = ''
point2 = ''
ind1 = ''
ind2 = ''
maxi = 0
with open('08.txt', 'r') as inf:
    for line in inf:
        mas.append(line.strip().split())
for i in range(len(mas)):
    if int(mas[i][4]) > maxi:
        maxi = int(mas[i][4])
        point1 = mas[i][0]
        point2 = mas[i][2]
        a = i
mas.pop(a)
lenh += maxi
maxi = 0
for i in range(len(mas)):
    if mas[i][0] == point1 or mas[i][0] == point2:
        if int(mas[i][4]) > maxi:
            maxi = int(mas[i][4])
            ind1 = mas[i][0]
            ind2 = mas[i][2]
            a = i
    if  mas[i][2] == point1 or mas[i][2] == point2:
        if int(mas[i][4]) > maxi:
            maxi = int(mas[i][4])
            ind1 = mas[i][2]
            ind2 = mas[i][0]
            a = i
mas.pop(a)
lenh += maxi 
maxi = 0
for i in range(len(mas)):
    if mas[i][0] == ind1 or mas[i][0] == ind2:
        if int(mas[i][4]) > maxi:
            maxi = int(mas[i][4])
            ind1 = mas[i][0]
            ind2 = mas[i][2]
            a = i
    if  mas[i][2] == ind1 or mas[i][2] == ind2:
        if int(mas[i][4]) > maxi:
            maxi = int(mas[i][4])
            ind1 = mas[i][2]
            ind2 = mas[i][0]
            a = i
mas.pop(a)
lenh += maxi

print(maxi)
print(lenh)