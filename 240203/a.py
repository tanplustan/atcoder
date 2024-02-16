S = input()
idx = S.find(".")
while idx != -1:
    idx = S.find(".")
    S = S[idx+1:]
print(S)