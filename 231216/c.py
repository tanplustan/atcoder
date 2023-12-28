N = int(input())
repyu = [1, 11, 111, 1111, 11111, 111111, 1111111, 11111111, 111111111, 1111111111, 11111111111, 111111111111]
total_repyu = []
x = 3
for i in range(0,12):
    for j in range(0,12):
        for k in range(0,12):
            total_repyu.append(repyu[k]+repyu[j]+repyu[i])
total_repyu = sorted(set(total_repyu))
print(total_repyu[N-1])
