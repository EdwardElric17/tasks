import re
mas = []
lst = ''
index = ''
c = 0
count_mark = 1
o = ''
a = 0
b = 0
s = 0
n = 0
q = 0
with open('10.txt', 'r') as inf:
    index = inf.readline().strip()
    lst = (re.split(r'[ ,\(\)]+', index))
    lst.pop(0)
print(lst)
count_let = 0
for i in lst:
    for j in i:
        if j.isdigit() == True:
            break
        else:
            count_let += 1
for i in range(len(lst)):
    s = 0
    for j in lst[i]:
        if j.isdigit() == True:
            mas.append(lst[i])
            break
        if j.isdigit() != True:
            o = ''
            if len(mas) == 1:
                for k in mas[0]:
                    if k != 'x':
                        o += k 
                        s = 1
                    else:
                        a = int(o)
                        count_let -= a
                        o = ''
                count_let += a*int(o)
            if s == 1:
                mas = []
            if len(mas) > 1:
                o = ''
                for k in range(len(mas)):
                    q = 0
                    n = 0
                    if mas[k] == mas[-1]:
                        for e in mas[k]:
                            if e != 'x':
                                o += e
                            else:
                                a = int(o)
                                count_let -= a
                                o = ''
                        count_mark *= a*int(o)
                        q = 1
                    else:
                        for e in range(len(mas[k])):
                            if mas[k][e-1] == 'x':
                                n = 1
                            if n == 1:
                                o += mas[k][e]
                        l = o
                        o = ''
                    if n == 1:
                        count_mark *= int(l)
                count_let += count_mark
                mas = []
print(count_let)
                    