Q = int(input())
A = []
for i in range(Q):
    a, b = map(int, input().split())
    if a == 1:
        A.append(b)
    else:
        print(A[len(A)-b])