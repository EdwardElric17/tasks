mas = [[0 for i in range(50)] for j in range(6)]
size = ''
with open('07.txt', 'r') as inf:
    for line in inf:
        m = (line.strip().split())
        a = 0
        b = 0
        x = 0
        x_shift = 0
        y = 0
        y_shift = 0
        m_y = []
        m_x = []
        if m[0] == 'rect':
            size = m[1]
            if len(size) == 3:
                a = int(size[0])
                b = int(size[2])
            else:
                if size[1] == 'x':
                    a = int(size[0])
                    b = int(size[2] + size[3])
                elif size[2] == 'x': 
                    a = int(size[0] + size[1])
                    b = int(size[3])
            for i in range(b):
                for j in range(a):
                    mas[i][j] = 1   
        if m[0] == 'rotate' and m[1] == 'row':
            y = int(m[2][2])
            y_shift = int(m[4])
            m_y = mas[y]
            mas[y] = m_y[-y_shift:] + m_y[:-y_shift]
        if m[0] == 'rotate' and m[1] == 'column':
            if len(m[2]) == 3:
                x = int(m[2][2])
            else:
                x = int(m[2][2] + m[2][3])
            x_shift = int(m[4])
            for i in range(6):
                m_x.append(mas[i][x])
            for i in range(6):
                mas[i][x] = m_x[i - x_shift]
for i in range(6):
    print(mas[i])
count = 0
for i in range(6):
    for j in range(50):
        if mas[i][j] == 1:
            count += 1
print(count)