point = ''
def search(start, end, lst, sum):
    global point
    for i in range(start, end):
        for j in range(1, end):
            if int(lst[i]) + int(lst[i + j]) == sum:
                point = str(lst[i] + ', ' + lst[i+j])
                k = i
                m = i + j
                search(k, m, lst, sum)
    return point
with open("04.txt", 'r') as inf:
    lst = inf.readline().split(', ')
print(search(0, len(lst)-1, lst, 77))