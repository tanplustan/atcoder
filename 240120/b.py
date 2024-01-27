S = input()
for i in range(len(S)):
    if S[i] == "A":
        pass
    else:
        for j in range(i, len(S)):
            if S[j] == "B":
                pass
            else:
                for k in range(j, len(S)):
                    if S[k] == "C":
                        pass
                    elif S[k] == "A" or S[k] == "B":
                        print("No")
                        exit()
print("Yes")