m = []
a = ''
b = ''
g = 0
h = 0
with open('05.txt', 'r') as inf:
    for line in inf:
        m = []
        m += (line.strip().split())
        g = 0
        for i in range(len(m) - 1):
            for j in range(i+1, len(m)):
                a = ''.join(sorted(m[i]))
                b = ''.join(sorted(m[j]))
                if a == b:
                    g += 1
        if g == 0 :
            h += 1
print(h)