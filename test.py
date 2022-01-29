mas = [[0 for i in range(50)] for j in range(6)]
size = ''
a = 0
b = 0
x = 0
x_shift = 0
y = 0
y_shift = 0
m_y = []
m_x = []
for lst in range(5):
    m = (input().split())
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
        print(m_y)