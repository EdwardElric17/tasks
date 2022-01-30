import re
mas = []
lst = ''
index = ''
acces1 = 0
acces2 = 0 
count = 0
with open('09.txt', 'r') as inf:
    for line in inf:
        lst = line.strip()
        index = re.split(r'[ ,\[\]]+', lst)
        mas.append(index)
for i in mas:
    acces1 = 0
    acces2 = 0
    for j in range(len(i)):
        if (j+1) % 2 == 0:
            for k in range(0, len(i[j])-3):
                if (i[j][k] + i[j][k+1] == i[j][k+3] + i[j][k+2]) and (i[j][k] != i[j][k+1]):
                    acces2 = 1
        else:
            for k in range(0, len(i[j])-3):
                if (i[j][k] + i[j][k+1] == i[j][k+3] + i[j][k+2]) and (i[j][k] != i[j][k+1]):
                    acces1 = 1
    if acces1 == 1 and acces2 != 1:
        count += 1
print(count)