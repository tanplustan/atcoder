N = int(input())
n = bin(N)
cnt = 0
while True:
    if n[-1] == "0":
        n = n[:-1]
        cnt += 1
    else:
        break
print(cnt)