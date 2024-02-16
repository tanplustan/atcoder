S = input()
lst = []
for i in range(97,123):
    lst.append(S.count(chr(i)))
for j in range(len(lst)):
    if lst[j] == max(lst):
        print(chr(j+97))
        break