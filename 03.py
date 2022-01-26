panel = [['1'], ['2','3','4'], ['5', '6', '7', '8', '9'], ['A', 'B', 'C'], ['D']]
cursor = '5'
code = ''
doc = []
with open("03.txt", 'r') as inf:
    for line in inf:
        doc.append(line.strip())
def code_searcher(m , n, cursor, code):
    for i in doc:
        for j in i:
            if j == 'U':
                if cursor not in  ('1', '2', '5', '4', '9'):
                    m -= 1
                    if m < 2:
                        n -= 1
                    else:
                        n += 1
                    cursor = panel[m][n]
            elif j == 'D':
                if cursor not in ('5', '9', 'A', 'C', 'D'):
                    m += 1
                    if m > 2:
                        n -= 1
                    else:
                        n += 1
                    cursor = panel[m][n]
            elif j == 'R':
                if cursor not in ('1', '4', '9', 'C', 'D'):
                    n += 1
                    cursor = panel[m][n]
            elif j == 'L':
                if cursor not in ('1', '2', '5', 'A', 'D'):
                    n -= 1
                    cursor = panel[m][n]
        code += cursor
    return code
print(code_searcher(2, 0, cursor, code))