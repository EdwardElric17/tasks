two_pereat = 0
three_repeat = 0
m = []
count = 0
cnt2 = 0
cnt3 = 0
with open("02.txt", 'r') as inf:
    for line in inf:
        m.append(line.strip())
for l in m:
    lst1 = ''
    lst2 = ''
    cnt2 = 0
    cnt3 = 0
    for i in l:    
        if i not in lst1:
            lst1 += i
        lst2 += i
    for i in lst1:
        count = 0
        for j in lst2:
            if j == i:
                count += 1
        if count == 2 and cnt2 == 0:
            cnt2 = 2
            two_pereat += 1
        elif count == 3 and cnt3 == 0:
            cnt3 = 2
            three_repeat += 1
print(two_pereat*three_repeat)