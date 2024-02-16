N = int(input())
A = list(map(int, input().split()))
B = [0]*N
s = 0
for i in range(N):
    s += A[i]
    B[i] = s
if all((x >= 0 for x in B)):
    print(B[N-1])
else:
    print(B[N-1]-min(B))
