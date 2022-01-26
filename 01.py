floor = 0
lst = str(input())
for i in lst:
    if i == '(':
        floor += 1
    else: 
        floor -= 1
print(floor)