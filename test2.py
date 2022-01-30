lst = ''
with open('10.txt', 'r') as inf:
    lst = inf.readline()
count1 = 0
count2 = 0
for i in lst:
    if i == '(':
        count1 += 1
    elif i == ')':
        count2 += 1
print(count1)
print(count2)