N = int(input())
Q = list(map(int,input().split()))
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = 0
i = 0
j = 0
l = 0
while i>=0:
    for k in range(N):
        if Q[k] <= A[k]*i + B[k]*j:
            l += 1
    print(l)
    if l == N-1:
        cnt = max(cnt,i+j)
        i+=1
        l+=1
    else:
        break
print(cnt)