def search(end, lst, sum):
    i = 0
    j = 1
    point = ''
    while i <= end:
        while j <= end:
            if int(lst[i]) + int(lst[i + j]) == sum:
                point = str(lst[i] + ', ' + lst[i+j])
                end = j + i
                i += 1
                j = 1
                break
            else:
                j += 1
        if j == end:
            i += 1
            j = 1
    return point
with open("04.txt", 'r') as inf:
    lst = inf.readline().split(', ')
print(search(len(lst)-1, lst, 77))