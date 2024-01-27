N = int(input())
A = list(map(int, input().split()))
dict = {}
for i, num in enumerate(A):
    dict[num] = i + 1

ans = [dict[-1]]

for i in range(N - 1):
    ans.append(dict[ans[i]])

ans_str = ' '.join(map(str, ans))
print(ans_str)