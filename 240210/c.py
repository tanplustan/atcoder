N = int(input())
l = [N]
total = 0
while max(l)>1:
    total += sum(l)
    li = []
    for num in l:
        li.extend([num // 2, (num + 1) // 2])
    l = li.copy()
    if 1 in l:
        l.remove(1)
print(total)