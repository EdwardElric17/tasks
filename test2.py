from sympy import powsimp


point = ''
def search(start, end, lst, sum):
    global point
    for i in range(start + 1, end):
        for j in range(1, end):
            if int(lst[i]) + int(lst[i + j]) == sum:
                point = str(lst[i] + ', ' + lst[i+j])
                print(point)
                print('i: ' + str(i))
                print('j: ' + str(j))
                k = i
                m = i + j - 1
                search(k, m, lst, sum)
                return None
            if j + i == end:
                break
with open("04.txt", 'r') as inf:
    lst = inf.readline().split(', ')
search(-1, len(lst)-1, lst, 77)