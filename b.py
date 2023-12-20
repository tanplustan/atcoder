S = input()
T = input()
Slen = sorted(S)
Tlen = sorted(T)
if Slen == ['A', 'B'] | ['A', 'E'] | ['B', 'A'] | ['B', 'C'] | ['C', 'B'] | ['C', 'D'] | ['D', 'C'] | ['D', 'E'] | ['E', 'A'] | ['E', 'D'] :
    s = 1
else:
    s = 2
    
if Tlen == ['A', 'B'] | ['A', 'E'] | ['B', 'A'] | ['B', 'C'] | ['C', 'B'] | ['C', 'D'] | ['D', 'C'] | ['D', 'E'] | ['E', 'A'] | ['E', 'D'] :
    t = 1
else:
    t = 2

if s == t:
    print("Yes")
    
else:
    print("No")
