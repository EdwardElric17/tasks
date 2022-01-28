with open("04.txt", 'r') as inf:
    lst = inf.readline().split(', ')
for i in range(len(lst)):
    if int(lst[i]) > 22 and int(lst[i]) < 60:
        print(i)
        print(lst[i])
        break