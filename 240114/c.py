N = int(input())
l = []
i = 0
while len(l) < N:
    if "1" in str(i) or "3" in str(i) or "5" in str(i) or "7" in str(i) or "9" in str(i):     
        i += 2  
    else:
        l.append(i)
        i += 2
print(l[N-1])
#TLE、、、、