S = input()
if S[0].isupper():
    S = S[1:]
    if S.islower():
        print("Yes")
    elif S == "":
        print("Yes")
    else:
        print("No")
else:
    print("No")