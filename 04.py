def search(start, end, lst, sum):
    for i in range(start + 1, end):
        for j in range(1, end):
            if int(lst[i]) + int(lst[i + j]) == sum:
                print(lst[i] + ', ' + lst[i+j])
                k = i
                m = i + j
                search(k, m, lst, sum)
with open("04.txt", 'r') as inf:
    lst = inf.readline().split(', ')
search(-1, len(lst)-1, lst, 77)